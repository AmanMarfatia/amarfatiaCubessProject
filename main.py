import sys
from urllib3.util import url
import requests
from secrets import wufoo_key
from requests.auth import HTTPBasicAuth

def get_wufoo_data() -> dict:
    url = "https://comp490project.wufoo.com/api/v3/forms/2023-ultimate-frisbee-tournament/entries/json"
   # http:/comp490project.wufoo.com/api/v3/forms/{identifier}/comments/count.json
   # https://comp490project.wufoo.com/api/v3/forms/2023-ultimate-frisbee-tournament/entries/json

    response = requests.get(url, auth=HTTPBasicAuth(wufoo_key, 'pass'))
    if response.status_code != 200:  # if we don't get an ok response we have trouble
        print(f"Failed to get data, response code:{response.status_code} and error message: {response.reason} ")
    sys.exit(-1)

    jsonresponse = response.json()
    return jsonresponse  # json response will be either a dictionary or a list of dictionaries
    # each dictionary represents a json object
def main():
    alldata = get_wufoo_data()
    print(alldata)

if __name__ =="__main__":
    main()
