# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 14:06:25 2016

@author: tmazaev
"""
import urllib
import json

#retrieve json string from input url
url = raw_input('Enter location: ')
print("Retrieving: " + url)
json_data = urllib.urlopen(url).read()
print('Retrieved ' + str(len(json_data)) + ' characters')

#parse json
data = json.loads(json_data)

#look for counts
counts = []
print(data)
for item in data:
    counts.append(item['count'])
    
counts = [int(count.text) for count in counts]
#and print result
print('Count: ' + str(len(counts)))
print('Sum: ' + str(sum(counts)))