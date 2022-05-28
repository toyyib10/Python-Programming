#!/usr/bin/env python
# coding: utf-8

# In[14]:


collection_list = []
while True:
    list_numbers = input('Enter a number: ')
    if list_numbers != 'done':
        try:
            list_value = float(list_numbers)
            collection_list.append(list_numbers)
            maximum = max(collection_list)
            minimum = min(collection_list)
        except:
            print('Bad Score')
            continue
    else:
        print('done!')
        break
print('Maximum: ', maximum)
print('Minimum', minimum)

