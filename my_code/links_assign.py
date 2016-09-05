# -*- coding: utf-8 -*-
# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

"""
Created on Thu Sep  1 20:08:24 2016

@author: tmazaev
"""

import urllib
from BeautifulSoup import *

url = raw_input('Enter url: ')
count = int(raw_input('Enter count: '))
position = int(raw_input('Enter position: '))

print "Retrieving:",url
 
for i in range(0,count):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    #retrieve all anchor tags
    tags = soup('a')
    links = list()
    for tag in tags:
        links.append(tag.get('href', None))
    url = str(links[position-1])
    print "Retrieving:",url