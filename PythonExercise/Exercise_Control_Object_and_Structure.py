#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Answer the following questions
#Write (or just say out loud to yourself) a brief description of all the following Object Types and Data Structures 
#we've learned about. You can edit the cell below by double clicking on it. Really this is just to test if you know the difference between these, so feel free to just think about it, since your answers are self-graded.

#Numbers - store numerical informations - numbers and floats
#Strings - Ordered sequence of characters wrapped inside single, double and tripple quotes
#Lists - Ordered sequence of objects. Lists are mutable.
#Tuples - Ordered sequence of objects. Tuples are immutable.
#Dictinaries - Random ways to store variables with key value pairs. easy to grab. can't be sorted


# In[ ]:


#Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25


# In[7]:


((6**2)/2)+83-0.75


# In[ ]:


#Answer these 3 questions without typing code. Then type code to check your answer.
#What is the value of the expression 4 * (6 + 5)?
#What is the value of the expression 4 * 6 + 5? 
#What is the value of the expression 4 + 6 * 5?


# In[8]:


4*(6+5)


# In[9]:


4*6+5


# In[10]:


4+6*5


# In[ ]:


#What is the type of the result of the expression 3 + 1.5 + 4?
#What would you use to find a number’s square root, as well as its square?


# In[12]:


3+1.5+4 #float


# In[23]:


n = 4
x = n**2
x


# In[30]:


import math


# In[34]:


math.sqrt(4)


# In[35]:


n = 4
x = math.sqrt(4)
x


# In[ ]:


#Given the string 'hello' give an index command that returns 'e'.


# In[37]:


s = 'hello'
s[1]


# In[ ]:


#Reverse the string 'hello' using slicing:


# In[3]:


s = 'hello'
s[::-1]


# In[ ]:


#Given the string hello, give two methods of producing the letter 'o' using indexing.


# In[4]:


s = 'hello'
s[4]


# In[5]:


s[-1]


# In[ ]:


#Problem - Build this list [0,0,0] two separate ways.


# In[32]:


#Method 1
[0]*3


# In[34]:


#Method 2
list2 = [0,0,0]
list2


# In[ ]:


#Problem - Reassign 'hello' in this nested list to say 'goodbye' instead:


# In[6]:


list3 = [1,2,[3,4,'hello']]
list3[2][2] = 'goodbye'


# In[7]:


list3


# In[3]:


list4 = [5,3,4,6,1]
list4.sort()


# In[ ]:


#Problem - Sort the list below:


# In[4]:


list4


# In[35]:


list5 = [10, 99, 1, 3, 500]
sorted(list5)


# In[ ]:


#Problem - Using keys and indexing, grab the 'hello' from the following dictionaries:


# In[5]:


d = {'simple_key':'hello'}
d['simple_key']


# In[6]:


d = {'k1':{'k2':'hello'}}
d['k1']['k2']


# In[14]:


d = {'k1':[{'nest_key':['this is deep',['hello']]}]}


# In[16]:


d['k1'][0]['nest_key'][1][0]


# In[17]:


d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}


# In[19]:


d['k1'][2]['k2'][1]['tough'][2][0]


# In[ ]:


#Problem - Can you sort a dictionary? Why or why not?


# In[20]:


#we can't sort a diectionary because it is not sequenced, rather it is mapping.


# In[ ]:


#Problem - What is the major difference between tuples and lists?


# In[21]:


#Tuples are immutable but Lists are mutable. Tuples use parenthesis but lists use square bracket.


# In[ ]:


#Problem - How do you create a tuple?


# In[22]:


#Tuples are created in parenthesis where stored items are separated by commas


# In[ ]:


#Problem - What is unique about a set?


# In[23]:


#set only shows uniqe elements


# In[ ]:


#Problem - Use a set to find the unique values of the list below:


# In[24]:


list5 = [1,2,2,33,4,4,11,22,3,3,2]
set(list5)


# In[25]:


# Answer before running cell 2 > 3. False
# Answer before running cell3 <= 2. False
# Answer before running cell 3 == 2.0. False
# Answer before running cell 3.0 == 3. True
# Answer before running cell 4**0.5 != 2. False


# In[26]:


2 > 3


# In[27]:


3 <= 2


# In[28]:


3 == 2.0


# In[29]:


3.0 == 3 #the hold the same value that is waht python cares about


# In[30]:


4**0.5 != 2 


# In[31]:


l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]
l_one[2][0] >= l_two[2]['k1']


# In[ ]:




