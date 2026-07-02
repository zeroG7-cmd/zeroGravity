#-------------------#
#Import             #
#--------------------#
import os
import sqlite3
import panda
from datetime import datetime

#
# Path File/Configuration #
#

#base 
SCRIPT_DIR = os.path.dirname(__FILE__)
BASE_DIR = os.path.dirname(SCRIPT_DIR)


#database
DB_PATH = os.path.join(BASE_DIR, "database", "zeroGravity.db")

#data
DATA_DIR = os.path.join(BASE_DIR, "data")



SPREADSHEET_ID = "1VNgzAnv02Tc0MmexAUv36w3hkJbC13HrAjP7Aqdnctc"

RANGE_NAME = 

EXPORT_DIR = os.path.join()

CREDENTIALS_PATH = 

#
# Database Function
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