# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 19:44:30 2016

@author: tmazaev
"""

# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('span')
int_list = list()

for tag in tags:
    # Look at the parts of a tag
    s = str(tag)
    extrac_ints = re.findall('([0-9]+)',s)
    ints = [int(s) for s in extrac_ints]
    int_list.extend(ints)
    
print 'Count: ',len(int_list)
print 'Sum: ',sum(int_list)