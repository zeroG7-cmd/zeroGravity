import pandas as pd
import sqlite3

# Read CSV file
data = pd.read_csv("data/survey.csv")

# Connect to SQLite database
conn = sqlite3.connect("database/zeroGravity.db")

# Move data into database
data.to_sql("survey_results", conn, if_exists="replace", index=False)

print("Survey data imported successfully!")
