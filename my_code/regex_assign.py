# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 12:19:56 2016

@author: tmazaev
"""

import re

data = open('regex_sum_42.txt')

int_list = list()

for line in data:
    extrac_ints = re.findall('([0-9]+)',line)
    ints = [int(s) for s in extrac_ints]
    int_list.extend(ints)
    
print(sum(int_list))