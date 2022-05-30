#!/usr/bin/env python
# coding: utf-8

# In[1]:


import string
fileName = input('Enter Name of File: ')
try:
    file = open(fileName)
except:
    print('Unable to open file')
    exit()
file = file.read()
for opened_file in file:
    opened_file = file.strip()
opened_file = opened_file.translate(opened_file.maketrans(' ',' ',string.punctuation))
opened_file = opened_file.lower()
words = opened_file.split()
count = 0
dictionary = dict()
for key in words:
    if key == 'sun' or key == 'mon' or key == 'tue'or key == 'wed' or key == 'thu' or key == 'fri' or key == 'sat':
        if key not in dictionary:
            dictionary[key] = 1 
        else:
            dictionary[key] += 1
print(dictionary)

