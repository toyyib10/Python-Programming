#!/usr/bin/env python
# coding: utf-8

# In[6]:


maximumValue = None
minimumValue = None
count = 0
total = 0
while True:
    value = input('Enter a starting value: ')
    if value != 'done':
        try:
            value = float(value)
            listValue = []
            count = count + 1
            listValue.append(value)
            for iterval in listValue:
                if maximumValue is None or iterval > maximumValue:
                    maximumValue = iterval
                if minimumValue is None or iterval < minimumValue:
                    minimumValue = iterval
                total = total + value
        except:
            print('Bad Score')
            continue
    else:
        print('done!')
        break
print(total ,count , 'maximum number: ', maximumValue, 'minimum number: ', minimumValue)
