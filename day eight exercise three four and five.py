#!/usr/bin/env python
# coding: utf-8

# In[5]:


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
print(dictionary)


# In[18]:


#exercise four
mostEmail = None
lst = list(dictionary.keys())
lst.sort()
for key in lst:
    if mostEmail is None or dictionary[key] > mostEmail:
        mostEmail = dictionary[key]
print(key, mostEmail)


# In[22]:


# exercise five
domainName = dict()
name = list(dictionary.keys())
name.sort()
for key in name:
    value = key.find('@')
    value = key[value + 1:]
    domainName[value] = dictionary[key]
print(domainName)

