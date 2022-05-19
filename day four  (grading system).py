#!/usr/bin/env python
# coding: utf-8

# In[5]:


# exercise 7
grades = input('Enter Grade: ')
def computegrade(grades):
    grade = grades
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
        print('Error, please input numeric value')
computegrade(grades)

