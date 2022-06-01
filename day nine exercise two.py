#!/usr/bin/env python
# coding: utf-8

# In[28]:


fhand = open('mbox-short.txt')
data = list()
for line in fhand:
    if line.startswith('From:'):
        continue
    elif line.startswith('From'):
        line = line.translate(line.maketrans(' ',' ','!"#$%&\'()*+,-./;<=>?@[\\]^_`{|}~'))
        data.append(line)
data.sort()
hours = dict()
for li in data:
    if ':' in li:
        val = li.find(':')
        key = li[val-2:val]
        if key not in hours:
            hours[key] = 1
        else:
            hours[key] += 1
lst = list(hours.keys())
lst.sort()
for key in lst:
    print(key,hours[key])

