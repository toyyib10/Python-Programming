#!/usr/bin/env python
# coding: utf-8

# In[1]:


words = open('words')
word = words.read()
type(word)
splited_word = word.split()
dictionary = dict()
for ch in splited_word:
    if ch not in dictionary:
        dictionary[ch] = 1
    else:
        dictionary[ch] = dictionary[ch] + 1
print(dictionary)

