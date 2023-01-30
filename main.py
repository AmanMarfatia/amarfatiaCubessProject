import sys
#import json
import requests
#import urllib2

'''
base_url = 'https://comp490project.wufoo.com/api/v3/'
username = 'G0QW-6YXP-H7LX-TN6S'
password = 'comp490'

password_manager = urllib2.HTTPPasswordMgrWithDefaultRealm()
password_manager.addpassword(None, base_url, username, password)
handler = urllib2.HTTPBasicAUthHandler(password_manager)
opener = urllib2.build_opener(handler)
urllib2.install_opener(opener)

response = urllib2.urlopen(base_url+'forms.json')
data = json.load(response)
print json.dumps(data, indent=4, sort_keys=True)
'''
from secrets import wufoo_key
from requests.auth import HTTPBasicAuth

def get_wufoo_data()->dict:
    url = "https://comp490project.wufoo.com/forms/2023-ultimate-frisbee-tournament/json"
    response = requests.get(url, auth=HTTPBasicAuth(wufoo_key,'pass'))
    if response.status_code != 200:
        print(f"Failed to get data, response code:{response.status_code} and error message:{response.reason}")
        sys.exit(-1)
    jsonresponse = response.json()
        return jsonresponse

