# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 14:06:25 2016

@author: tmazaev
"""
import urllib
import re

#retrieve json string from input url
url = raw_input('Enter location: ')
print("Retrieving: " + url)
data = urllib.urlopen(url).read()
print('Retrieved ' + str(len(data)) + ' characters')

#look for counts
int_list = []
extrac_ints = re.findall('([0-9]+)',data)
ints = [int(s) for s in extrac_ints]
int_list.extend(ints)
    
#and print result
print('Count: ' +  str(len(int_list)))
print('Sum: ' + str(sum(int_list)))