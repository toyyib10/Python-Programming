#!/usr/bin/env python
# coding: utf-8

# In[66]:


# exercise one
def chop(frt):
    frt[1 : len(letters) - 1]
    return None
fruits = ['apple', 'banana', 'mango', 'pineapple']
fruit = chop(fruits)
print(fruit)


# In[94]:


def middle(c):
    return c[1 : len(cars) - 1]
cars = ['Honda', 'Toyota', 'Rav','BMW', 'Chevrolet']
print(len(cars))
car = middle(cars)
print(car)


# In[40]:


fhand = open('untitled1.txt')
print(fhand)
inp = fhand.read()
print(len(inp))
#for char in inp:
    # v = char
print(inp[:266])
inp.count('uu')
t = 'toyyib'
s = list(t)
print(s[0:3])
t = ['pining', 'for', 'the', 'fjords']
delimiter = ' '
delimiter.join(t)
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    print(words[2])

