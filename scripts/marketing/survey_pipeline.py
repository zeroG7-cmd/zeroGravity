#-------------------#
#Import             #
#--------------------#
import os
import sqlite3
from panda import pd
from datetime import datetime

from google.oauth2 import service_account
from googleapiclient.discovery import build
#
# Path File/Configuration #
#

#base 
SCRIPT_DIR = os.path.dirname(__file__)
BASE_DIR = os.path.dirname(SCRIPT_DIR)


#database
DB_PATH = os.path.join(BASE_DIR, "database", "zeroGravity.db")

#data
DATA_DIR = os.path.join(BASE_DIR, "data")

RAW_DIR = os.path.join(DATA_DIR, "raw")
EXPORT_DIR = os.path.join(DATA_DIR, "exports")
ARCHIVE_DIR = os.path.join(DATA_DIR, "archive")

CREDENTIALS_PATH = os.path.join(BASE_DIR, "credentials", "google_credentials.json")
SPREADSHEET_ID = "1VNgzAnv02Tc0MmexAUv36w3hkJbC13HrAjP7Aqdnctc"



RANGE_NAME = 

scope = 




#
# Database Function

def connect_db():

def create_test_logs_table():


def setup_database():
    pass


def fetch_survey_responses():
    pass


def save_survey_responses():
    pass


#Export Function 
def export_survey_snapshot():
    pass



#Main Runner
def main():
    setup_database()
    responses = fetch_survey_responses()
    save_survey_responses(responses)
    export_survey_snapshot()


if __name__ == "__main__":
    main()