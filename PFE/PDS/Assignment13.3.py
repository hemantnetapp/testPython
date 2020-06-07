'''
Calling a JSON API

In this assignment you will write a Python program that will prompt for a location, contact a web service and retrieve JSON for the
web service and parse that data, and retrieve the first place_id from the JSON. A place ID is a textual identifier that uniquely identifies
a place as within Google Maps.

http://py4e-data.dr-chuck.net/json?

To call the API, you need to include a key= parameter and provide the address that you are requesting as the address= parameter that is
properly URL encoded using the urllib.parse.urlencode() function
'''


import urllib.request, urllib.parse, urllib.error
import json
api_key = False
if api_key is False:
    api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/json?'
address = input('Enter location: ')
if len(address) < 1:
    print("Try again with passing correct URL")
    exit()
#to encode address adding it to dictionary and preparing entire url
parms = dict()
parms['address'] = address
if api_key is not False: parms['key'] = api_key
url = serviceurl + urllib.parse.urlencode(parms)
#printing the prepared url
print('Retrieving ',url)
#read the given url and count and print total number of characters
urlData = urllib.request.urlopen(url).read().decode('utf-8')
print('Retrieved', len(urlData), 'characters')

#parsing the data
try:
    info = json.loads(urlData)
except:
    info = None
if not info or 'status' not in info or info['status'] != 'OK':
    print('==== Failure To Retrieve ====')
    print(urlData)
    exit()

place_id=info["results"][0]["place_id"]
print('Place id ',place_id)


'''
Desired Output:
Enter location: South Federal University
Retrieving  http://py4e-data.dr-chuck.net/json?address=South+Federal+University&key=42
Retrieved 2505 characters
Place id  ChIJ0V94rPl_bIcRqLdrlbjFMDk
'''
