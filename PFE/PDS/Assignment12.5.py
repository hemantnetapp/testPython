'''
Scraping Numbers from HTML using BeautifulSoup In this assignment you will write a Python program.
The program will use urllib to read the HTML from the data files below, and parse the data, extracting numbers and compute the sum of the numbers in the file.

http://py4e-data.dr-chuck.net/comments_42.html

You are to find all the <span> tags in the file and pull out the numbers from the tag and sum the numbers.

Sample Execution:
$ python3 solution.py
Enter - http://py4e-data.dr-chuck.net/comments_42.html
Count 50
Sum 2...
'''

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup


url = input('Enter - ')
html = urllib.request.urlopen(url).read()
numberSoup = BeautifulSoup(html, 'html.parser')
count=0
sum=0
# Retrieve all of the span tags
tags = numberSoup('span')
for tag in tags:
    count=count+1
    sum=sum+int(tag.contents[0])
print ("Count ",count)
print ("Sum ",sum)


'''
Desired Output:
Enter -  http://py4e-data.dr-chuck.net/comments_42.html
Count  50
Sum  2553
'''
