#import requests

#response = requests.get('https://comp490project.wufoo.com/forms/2023-ultimate-frisbee-tournament')
#form = response.json()
#print(response.text)

import urllib2
import json

base_url = 'https://comp490project.wufoo.com/forms/2023-ultimate-frisbee-tournament/api/v3/'
username = 'G0QW-6YXP-H7LX-TN6S'
password = 'comp490'

password_manager = urllib2.HTTPPasswordMgrWithDefaultRealm()

handler = urllib2.HTTPBasicAUthHandler(password_manager)
opener = urllib2.build_opener(handler)
urllib2.install_opener(opener)

response = urllib2.urlopen(base_url+'forms.json')
data = json.load(response)
print(json.dumps(data, indent=4, sort_keys=True))



