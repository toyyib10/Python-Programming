#!/usr/bin/env python
# coding: utf-8

# In[7]:


fileName = input('File Name: ')
try:
    fName = open(fileName)
except:
    print('file does not exist')
    exit()
openedFile = fName.read()
import string
for line in openedFile:
    openedFile.strip()
    openedFile.translate(openedFile.maketrans(' ',' ',string.punctuation))
    line = openedFile.lower()
letters = list(line)
letterHistogram = dict()
letters.sort()
alphabelt = list(string.ascii_letters)
for letter in letters:
    if letter.isalpha():
        if letter not in letterHistogram:
            letterHistogram[letter] = 1
        else:
            letterHistogram[letter] += 1
lst = list()
for key, val in list(letterHistogram.items()):
    lst.append((val, key))
lst.sort(reverse=True)
for val, key in lst:
    print(key, val)

