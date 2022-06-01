#!/usr/bin/env python
# coding: utf-8

# In[25]:


fileName = input('Enter file name: ')
try:
    opened_file = open(fileName)
except:
    print("file doesn't exist")
    exit()
opened_file = opened_file.read()
for file in opened_file:
    file = opened_file.rstrip()
file = file.translate(file.maketrans(' ',' ','!"#$%&\'()*+,-/:;<=>?[\\]^_`{|}~'))
emailName = file.split()
dictionary = dict()
for key in emailName:
    if '@' in key:
        if key not in dictionary:
            dictionary[key] = 1
        else:
            dictionary[key] += 1
count = None
lstEmail = list()
for email,count in list(dictionary.items()):
    lstEmail.append((count,email))
lstEmail.sort(reverse = True)

for val, key in lstEmail[:1]:
    print(key, val)
#

