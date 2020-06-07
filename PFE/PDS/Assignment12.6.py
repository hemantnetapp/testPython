'''
write a Python program to extract the href= values from the anchor tags, scan for a tag that is in a particular position 
relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find.

 http://py4e-data.dr-chuck.net/known_by_Fikret.html
Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
Last name in sequence: Anayah
'''


import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup


url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))-1

html = urllib.request.urlopen(url).read()
hrefSoup = BeautifulSoup(html, 'html.parser')
# loop variale to fetch last name
loop=0
# Retrieve all of the anchor tags
tags = hrefSoup('a')
print('Retrieving: ',url)
for i in range(count):
    link=tags[position].get('href',None)
    print('Retrieving: ',tags[position].get('href', None))
    loop=loop+1
    if loop==count:
        break
    html = urllib.request.urlopen(link).read()
    hrefSoup = BeautifulSoup(html,'html.parser')
    tags = hrefSoup('a')
print('Last Name: ',tags[position].contents[0])

'''
Desired Output:
Enter URL: http://py4e-data.dr-chuck.net/known_by_Fikret.html
Enter count: 4
Enter position: 3
Retrieving:  http://py4e-data.dr-chuck.net/known_by_Fikret.html
Retrieving:  http://py4e-data.dr-chuck.net/known_by_Montgomery.html
Retrieving:  http://py4e-data.dr-chuck.net/known_by_Mhairade.html
Retrieving:  http://py4e-data.dr-chuck.net/known_by_Butchi.html
Retrieving:  http://py4e-data.dr-chuck.net/known_by_Anayah.html
Last Name:  Anayah
'''
