#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# exercise one
word = input('Enter a word: ')
index = 1
while index <= len(word): 
    letter = word[-index]
    print(letter)
    index = index + 1


# In[ ]:


# exercise two
frt =  'fruit'
frt[:]


# In[10]:


# exercise three
word = input('Enter a word to confirm the number of letter: ')
letter = input('Enter the letter you want to check: ')
def count(string,let):
    count = 0
    for alphabelt in string:
        if alphabelt == letter:
            count = count + 1
    print('number of',letter,'in',word ,'is',count)
count(word,letter)


# In[15]:


word = 'banana'
word.count('a')


# In[12]:


str = 'X-DSPAM-Confidence:0.8475'
startPoint = str.find('0')
print(startPoint)
endPoint = str.find('5')
print(endPoint)
value = str[startPoint : endPoint + 1]
print(value)
floatingValue = float(value)
type(floatingValue)


