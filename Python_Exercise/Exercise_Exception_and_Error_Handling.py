#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Problem 1 - Handle the exception thrown by the code below by using try and except blocks.
for i in ['a','b','c']:
    print(i**2)


# In[3]:


#Solution 1
try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
    print("There was a type error")


# In[5]:


#Problem 2
#Handle the exception thrown by the code below by using try and except blocks. 
#Then use a finally block to print 'All Done.'

x = 5
y = 0

z = x/y


# In[6]:


try:
    x = 5
    y = 0

    z = x/y
except ZeroDivisionError:
    print('There was a ZeroDivisionError')
    
finally:
    print("All done!")


# In[7]:


#Problem 3 - 
#Write a function that asks for an integer and prints the square of it. Use a while loop with a try, except, 
#else block to account for incorrect inputs.


# In[18]:


def square_of_int():
    
    while True:
        try:
            n = int(input("Please provide number: "))
        except:
            print("Whoops! That is not a number")
            continue
        else:
            print("yes, that's a number. Great job!")
            break
        finally:
            print("End of try/except/finally")
            
    print("Square of the number is: ")
    print(n**2)


# In[19]:


square_of_int()


# In[20]:


square_of_int()


# In[ ]:




