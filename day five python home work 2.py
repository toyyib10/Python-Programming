#!/usr/bin/env python
# coding: utf-8

# In[6]:


largest = None
smallest = None
count = 0
total = 0
while True:
    value = input('Enter a starting value: ')
    if value != 'done':
        try:
            vale = float(value)
            va = []
            count = count + 1
            va.append(vale)
            for val in va:
                if largest is None or val> largest:
                    largest = val
                if smallest is None or val < smallest:
                    smallest = val
                total = total + vale
        except:
            print('Bad Score')
            continue
    else:
        print('done')
        break
print(total ,count , 'maximum number: ', largest, 'minimum number: ', smallest)

