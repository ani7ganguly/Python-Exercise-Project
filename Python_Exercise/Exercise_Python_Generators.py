#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Problem 1
#Create a generator that generates the squares of numbers up to some number N.


# In[2]:


def gensquares(N):

    for num in range(N):
        yield(num)**2


# In[3]:


for x in gensquares(10):
    print(x)


# In[1]:


#Problem 2
#Create a generator that yields "n" random numbers between a low and high number (that are inputs).
#Note: Use the random library. For example:


# In[3]:


import random

def rand_num(low,high,N):

    for num in range(N):
        yield (random.randint(low,high))


# In[5]:


for num in rand_num(1,10,12):
    print(num)


# In[6]:


#Problem 3
#Use the iter() function to convert the string below into an iterator:


# In[1]:


s = 'hello'
s_iter = iter(s)
print(next(s_iter))


# In[ ]:


#Problem 4
#Explain a use case for a generator using a yield statement where you would not want to use a normal function with a return statement.


# In[ ]:


#If the output has the potential of taking up a large amount of memory and you only intend to iterate through it, 
#you would want to use a generator. (Multiple answers are acceptable here!)


# In[ ]:


#Problem 5


# In[ ]:


#Can you explain what gencomp is in the code below?


# In[25]:


my_list = [1,2,3,4,5]

gencomp = (item for item in my_list if item > 3)

for item in gencomp:
    print(item)


# In[ ]:


#a generator comprehension is like a list comprehension, but instead of finding all the items you're interested 
#and packing them into list, it waits, and yields each item out of the expression, one by one.


# In[26]:


my_list = [1,2,3,4,5]

for item in my_list:
    if item > 3:
        print(item)

