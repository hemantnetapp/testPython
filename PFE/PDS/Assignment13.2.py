'''
Write a program to that will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment
counts from the JSON data, compute the sum of the numbers in the file.

http://py4e-data.dr-chuck.net/comments_42.json

'''

import urllib.request, urllib.parse, urllib.error
import json


url = input('Enter location: ')
if len(url) < 1:
    print("Try again with passing correct URL")
print('Retrieving ',url)

#read the given url
urlData = urllib.request.urlopen(url).read().decode('utf-8')
print('Retrieved', len(urlData), 'characters')

info = json.loads(urlData)
print('Count: ',len(info))
sum=0
for eachNum in info["comments"]:
    sum+=int(eachNum['count'])

print('Sum: ',sum)

'''
Desired Output:
Enter location: http://py4e-data.dr-chuck.net/comments_42.json
Retrieving  http://py4e-data.dr-chuck.net/comments_42.json
Retrieved 2711 characters
Count:  2
Sum:  2553
'''
