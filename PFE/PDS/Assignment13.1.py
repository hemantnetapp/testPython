'''
Write a Python program to read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data,
compute the sum of the numbers in the file.

 http://py4e-data.dr-chuck.net/comments_42.xml
 
To make the code a little simpler, you can use an XPath selector string to look through the entire tree of XML for any tag named 'count'
with the following line of code:
counts = tree.findall('.//count')
Take a look at the Python ElementTree documentation and look for the supported XPath syntax for details. You could also work from the top
of the XML down to the comments node and then loop through the child nodes of the comments node.

'''

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl



url = input('Enter location: ')
if len(url) < 1:
    print("Try again with passing correct URL")
print('Retrieving ',url)

#read the given url
urlData = urllib.request.urlopen(url).read()
print('Retrieved', len(urlData), 'characters')

tree=ET.fromstring(urlData)
num=tree.findall('.//count')
print('Count: ',len(num))
sum=0
for eachNum in num:
    sum+=int(eachNum.text)

print('Sum: ',sum)

'''
Desired Output:
Enter location: http://py4e-data.dr-chuck.net/comments_42.xml
Retrieving  http://py4e-data.dr-chuck.net/comments_42.xml
Retrieved 4189 characters
Count:  50
Sum:  2553

'''
