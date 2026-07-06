#-------------------#
#Import             #
#--------------------#
import os
import sqlite3
from datetime import datetime

from google.oauth2 import service_account
from googleapiclient.discovery import build
#
# Path File/Configuration #
#

#base 
SCRIPT_DIR = os.path.dirname(__file__)
BASE_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))


#database
DB_PATH = os.path.join(BASE_DIR, "database", "zeroGravity.db")

#data
DATA_DIR = os.path.join(BASE_DIR, "data")

RAW_DIR = os.path.join(DATA_DIR, "raw")
EXPORT_DIR = os.path.join(DATA_DIR, "exports")
ARCHIVE_DIR = os.path.join(DATA_DIR, "archive")

CREDENTIALS_PATH = os.path.join(BASE_DIR, "credentials", "google_credentials.json")
SPREADSHEET_ID = "1VNgzAnv02Tc0MmexAUv36w3hkJbC13HrAjP7Aqdnctc"



RANGE_NAME = "Form Responses 1!A:Z"
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]





#
# Database Function

def fetch_survey_responses():
    creds = service_account.Credentials.from_service_account_file(
        CREDENTIALS_PATH, 
        scopes=SCOPES    
    )  
    
    service = build("sheets", "v4", credentials=creds)
    sheet = service.spreadsheets()
    result = sheet.values().get(
        spreadsheetId=SPREADSHEET_ID,
        range=RANGE_NAME
    ).execute()

    values = result.get("values", [])

    if not values:
        print("No data found.")
        return []

    headers = values[0]
    rows = values[1:]

    responses = []
    for row in rows:
        response = dict(zip(headers, row))
        responses.append(response)

    print(f"Fetched {len(responses)} survey responses.")
    return responses


def connect_db():
    conn = sqlite3.connect(DB_PATH)
    return conn

def create_responses_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
         CREATE TABLE IF NOT EXISTS customer_survey_responses (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             submitted_at TEXT UNIQUE,
             customer_type TEXT,
             used_drone_services TEXT,
             would_consider_drone_services TEXT,
             service_interest TEXT,
             key_buying_factor TEXT,
             budget_range TEXT,
             provider_choice_factor TEXT,
             additional_comments TEXT,
             imported_at TEXT
        )
    """)
    conn.commit()
    conn.close()

def setup_database():
    create_responses_table()

def transform_survey_response(response):
    return {
        "submitted_at": response.get("Timestamp"),
        "customer_type": response.get("  Q1. What best describes you?  "),
        "used_drone_services": response.get("Q2. Have you ever used drone services before?"),
        "would_consider_drone_services": response.get("Q3.  Would you consider using drone services?"),
        "service_interest": response.get("Q4. What would you most likely use drone services for?"),
        "key_buying_factor": response.get("Q5.  What matters most when choosing a service?"),
        "budget_range": response.get("  Q6.  How much would you be willing to pay for drone services? "),
        "provider_choice_factor": response.get("Q7.  What would make you choose a drone provider?"),
        "additional_comments": response.get("Q8. Any additional comments?"),
        "imported_at": datetime.now().isoformat(timespec="seconds"),
    }

def save_survey_responses(responses):
    conn = connect_db()
    cursor = conn.cursor()

    for response in responses:
        clean_response = transform_survey_response(response)

        cursor.execute("""
            INSERT OR IGNORE INTO customer_survey_responses (
                submitted_at,
                customer_type,
                used_drone_services,
                would_consider_drone_services,
                service_interest,
                key_buying_factor,
                budget_range,
                provider_choice_factor,
                additional_comments,
                imported_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            clean_response["submitted_at"],
            clean_response["customer_type"],
            clean_response["used_drone_services"],
            clean_response["would_consider_drone_services"],
            clean_response["service_interest"],
            clean_response["key_buying_factor"],
            clean_response["budget_range"],
            clean_response["provider_choice_factor"],
            clean_response["additional_comments"],
            clean_response["imported_at"],
        ))

    conn.commit()
    conn.close()

    print(f"Saved {len(responses)} survey responses.")


#Export Function 
def export_survey_snapshot():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM customer_survey_responses")
    total_responses = cursor.fetchone()[0]

    cursor.execute("""
        SELECT service_interest, COUNT(*)
        FROM customer_survey_responses
        GROUP BY service_interest
        ORDER BY COUNT(*) DESC
    """)
    service_interest_rows = cursor.fetchall()

    cursor.execute("""
        SELECT budget_range, COUNT(*)
        FROM customer_survey_responses
        GROUP BY budget_range
        ORDER BY COUNT(*) DESC
    """)
    budget_rows = cursor.fetchall()

    os.makedirs(EXPORT_DIR, exist_ok=True)

    export_path = os.path.join(EXPORT_DIR, "survey_snapshot.md")

    with open(export_path, "w", encoding="utf-8") as file:
        file.write("# ZeroGravity Survey Snapshot\n\n")
        file.write(f"Generated at: {datetime.now().isoformat(timespec='seconds')}\n\n")

        file.write(f"## Total Responses\n\n")
        file.write(f"{total_responses}\n\n")

        file.write("## Service Interest\n\n")
        for service_interest, count in service_interest_rows:
            file.write(f"- {service_interest}: {count}\n")

        file.write("\n## Budget Range\n\n")
        for budget_range, count in budget_rows:
            file.write(f"- {budget_range}: {count}\n")

    conn.close()

    print(f"Survey snapshot exported to: {export_path}")



#Main Runner
def main():
    setup_database()
    responses = fetch_survey_responses()
    save_survey_responses(responses)
    export_survey_snapshot()


if __name__ == "__main__":
    main()