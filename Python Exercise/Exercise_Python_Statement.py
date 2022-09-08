#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Problem - Print only the words that start with s in this sentence


# In[1]:


st = 'Print only the words that start with s in this sentence'
mylist = st.split()
for word in mylist:
    if (list(word))[0] == 's':
        print(word)


# In[2]:


#Alternate way
st = 'Print only the words that start with s in this sentence'
mylist = st.split()
for word in mylist:
    if word[0] == 's':
        print(word)
#you can use the indexing of string, much more readable


# In[ ]:


#Problem - Use range() to print all the even numbers from 0 to 10.


# In[3]:


for num in range(0,10):
    if num%2 == 0:
        print(num)


# In[ ]:


#Problem - Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.


# In[4]:


mylist = [num for num in range(1,50)]
for num in mylist:
    if num%3 == 0:
        print(num)


# In[ ]:


#Problem - Go through the string below and if the length of a word is even print "even!"
#st = 'Print every word in this sentence that has an even number of letters'


# In[5]:


st = 'Print every word in this sentence that has an even number of letters'
mylist = st.split()
for word in mylist:
    if len(word)%2 == 0:
        print('"even!"')


# In[ ]:


#Problem - Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of 
#          the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and 
#          five print "FizzBuzz".


# In[6]:


for num in range (1,100):
    if (num%3 == 0 and num%5 == 0):
        print('"FizzBuzz"')
    elif num%3 == 0:
        print('"Fizz"')
    elif num%5 == 0:
        print('"Buzz"')
    else:
        print(num)


# In[ ]:


#Problem - Use List Comprehension to create a list of the first letters of every word in the string below:
#          st = 'Create a list of the first letters of every word in this string'


# In[7]:


st = 'Create a list of the first letters of every word in this string'
[(list(item))[0] for item in st.split()]


# In[8]:


#Alternate solution
st = 'Create a list of the first letters of every word in this string'
[word[0] for word in st.split()]
#used word indexing, no to need make another list, more readable

