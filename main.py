import urllib2
import json

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

