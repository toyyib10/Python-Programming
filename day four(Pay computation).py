#!/usr/bin/env python
# coding: utf-8

# # exercise 6

# In[17]:


hours = input('Working Hours: ')
rates = input('Working Rate: ')
def computepay(hours,rates):
    hour = hours
    rate = rates
    try:
        h = float(hour)
        r = float(rate)
        def ps():
                p = (h * r)
                return p
        if h > 40:
            pays = ps() + 25
            print('Pay:',pays)
        else:
            print('Pay:',ps())
    except:
        print('Error, please input a numeric value')
computepay(hours,rates)

