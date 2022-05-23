#!/usr/bin/env python
# coding: utf-8

# In[14]:


total = 0
count = 0
while True:
    value = input('Enter a number: ')
    if value != 'done':
        try:
            val = float(value)
            total = val + total
            count = count + 1
            continue
        except:
            print('Bad Score') 
            continue
    else:
        print('done!')
        print(total, count, total/count)
        value = ' '
        break

