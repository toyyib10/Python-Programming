#!/usr/bin/env python
# coding: utf-8

# In[ ]:


hour = float(input('working hours: '))
rate = float(input('Rate: '))
if hour > 40:
    pay = hour * rate
    increasePay = pay + 25
    print('Pay: ',increasePay)
else:
    pay = hour * rate
    print('Pay:',pay)


# # exercise2

# In[ ]:


hours = input('working hour:')
rates = input('rate: ')
try:
    h = float(hours)
    r = float(rates)
    pay = h * r
    print('Pay:',pay)
except:
    print('Error, please enter numeric input')


# # exercise3

# In[6]:


grade = input('Enter Grade: ')
try:
    gd = float(grade)
    if gd >= 0.9 and gd < 1:
        print('A')
    elif gd >= 0.8 and gd < 0.9:
         print('B')
    elif gd >= 0.7 and gd < 0.8:
         print('C')
    elif gd >= 0.6 and gd < 0.7:
         print('D')
    elif gd < 0.6 and gd >= 0:
         print('F')
    elif gd >= 1:
         print('invalid input')
    elif gd < 0:
         print('invalid input')
    else:
         print('invalid input')
except:
    print('invalid input')

