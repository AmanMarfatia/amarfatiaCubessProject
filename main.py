import sys
from sqlite3 import Cursor

import requests
from secrets import wufoo_key
from requests.auth import HTTPBasicAuth
import json
import sqlite3

data1 = {'EntryId': '1', 'Field2': 'Dr.', 'Field8': '', 'Field9': '', 'Field10': '', 'Field11': '', 'Field12': '',
         'Field216': '', 'Field14': '', 'Field15': '', 'Field16': '', 'Field17': '', 'Field18': '', 'Field115': '',
         'Field116': '', 'Field117': '', 'Field118': '', 'DateCreated': '2023-01-27 19:43:55', 'CreatedBy': 'public',
         'DateUpdated': '', 'UpdatedBy': None}


def get_wufoo_data() -> dict:
    url = "https://comp490project.wufoo.com/api/v3/forms/2023-ultimate-frisbee-tournament/entries/json"

    response = requests.get(url, auth=HTTPBasicAuth(wufoo_key, 'pass'))
    if response.status_code != 200:  # if we don't get an ok response we have trouble
        print(f"Failed to get data, response code:{response.status_code} and error message: {response.reason} ")
        sys.exit(-1)

    jsonresponse = response.json()
    return jsonresponse  # json response will be either a dictionary or a list of dictionaries
    # each dictionary represents a json object


def file_save(data):
    with open("data.txt", "w") as file:
        file.write(json.dumps(data))


# make this a function where where it takes data as a parameter
# conn = sqlite3.connect('cube_database.sqlite')
print("Database conection")


def data_base_insert():
    conn = sqlite3.connect('/Users/amanmarfatia/PycharmProjects/amarfatiaCubessProject/cube_database.sqlite3')
    cursor: Cursor = conn.cursor()
    cursor.execute('''INSERT INTO 'cube_data' ( EntryId, Prefix, First, Last, Logo, TeamName, Email, JerseyColor, PhoneNumber, Coach, HeadCoach, Waterboys, Doctor, EighteenThruTwentyFive, TwentyfiveThruThirty, ThirtyThruForty, FortyThruFifty),
        VALUES(
        '1',
        'Dr',
        '',
        'Null',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        ''
        ''')

    conn.commit()
    conn.close()


print("Open database successfully")


def main():
    alldata = get_wufoo_data()
    # file_save(alldata)
    # print(alldata)
    array_of_entries = alldata["Entries"]

    for arr in array_of_entries:
        print(arr)

    data_base_insert()


if __name__ == "__main__":
    main()
