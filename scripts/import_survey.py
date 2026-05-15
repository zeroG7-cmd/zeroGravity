from pathlib import Path      # Handles file paths safely across Windows/Linux
import pandas as pd           # Used to read and manipulate CSV data
import sqlite3                # Built-in database engine (SQLite)

# ------------------------------------------------------------
# 1. Get the location of THIS script file
# ------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent
# __file__ = current script (import_survey.py)
# .resolve() = converts it to an absolute path
# .parent = gets the folder "scripts/"

# ------------------------------------------------------------
# 2. Build path to the CSV file (relative to project root)
# ------------------------------------------------------------
file_path = BASE_DIR / ".." / "data" / "survey_responses.csv"
# ".." means go up one folder (from scripts → zeroGravity)
# then enter data/ folder
# then find survey_responses.csv

# ------------------------------------------------------------
# 3. Load CSV into a DataFrame (like a spreadsheet in Python)
# ------------------------------------------------------------
data = pd.read_csv(file_path)
# Reads the CSV file into a pandas DataFrame (table structure)

# ------------------------------------------------------------
# 4. Connect to SQLite database
# ------------------------------------------------------------
db_path = BASE_DIR / ".." / "database" / "zeroGravity.db"
conn = sqlite3.connect(db_path)
# Opens (or creates) the SQLite database file

# ------------------------------------------------------------
# 5. Send DataFrame into SQLite as a table
# ------------------------------------------------------------
data.to_sql(
    "survey_responses",   # Table name inside database
    conn,                 # Database connection
    if_exists="replace",  # Replace table if it already exists
    index=False           # Do NOT write pandas index as a column
)

# ------------------------------------------------------------
# 6. Close database connection 
# ------------------------------------------------------------
conn.close()

print("CSV successfully imported into SQLite database.")
