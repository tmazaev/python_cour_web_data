# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 14:06:25 2016

@author: tmazaev
"""
import urllib
import xml.etree.ElementTree as ET

#retrieve xml string from input url
url = raw_input('Enter location: ')
print("Retrieving: " + url)
data = urllib.urlopen(url).read()
print('Retrieved ' + str(len(data)) + ' characters')

#parse xml into tree structure
tree = ET.fromstring(data)

#look for counts
counts = tree.findall('.//count')
counts = [int(count.text) for count in counts]
#and print result
print('Count: ' + str(len(counts)))
print('Sum: ' + str(sum(counts)))