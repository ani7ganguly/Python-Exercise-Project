#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Problem 1
# Construct a class methods to accept coordinates as a pair of tuples and return the slope and distance of the 
# line.


# In[1]:


#Let us to it by indexing first
class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        return (((self.coor2)[0] - (self.coor1)[0])**2 + ((self.coor2)[1] - (self.coor1)[1])**2)**0.5
    
    def slope(self):
        return ((self.coor2)[1] - (self.coor1)[1])/((self.coor2)[0] - (self.coor1)[0])


# In[2]:


line1 = Line((3,2),(8,10))


# In[3]:


line1.distance()


# In[21]:


line1.slope()


# In[6]:


#we can also do it by tuple unpacking
class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    
    def slope(self):
        
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return ((y2 - y1) / (x2 - x1))


# In[7]:


line2 = Line((3,2),(8,10))


# In[8]:


line2.distance()


# In[9]:


line2.slope()


# In[ ]:





# In[ ]:





# In[ ]:


# Problem 2
# Construct a class methods to accept height and radius to return the volume and surfac area.


# In[33]:


class Cylinder:
    
    def __init__(self,height,radius):
        
        self.height = height
        self.radius = radius
        
    def volume(self):
        return ((3.14)*((self.radius)**2)*(self.height))
    
    def surface_area(self):
        return (2*3.14*(self.radius)*(self.height) + 2*(3.14)*(self.radius**2))


# In[34]:


c = Cylinder(2,3)


# In[35]:


c.volume()


# In[29]:


c.surface_area()


# In[ ]:





# In[ ]:





# In[10]:


#Problem 3
#create a bank account class that has 

#two attributes: owner, balance and two methods: deposit, withdraw

#As an added requirement, withdrawals may not exceed the available balance.

#Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.


# In[87]:


class Account:
    
    def __init__(self,owner,balance):
        
        self.owner = owner
        self.balance = balance
        
    def owner(self,owner):
        
        self.owner = owner
        
    def __str__(self):
        
        return f"Account owner: {self.owner}" + f"\nAccount balance: {self.balance}"
        
    def deposit(self,amount):
        
        self.balance = self.balance + amount
        
        print ("Deosit Accepted")
        return (f"Your new balance is {self.balance}")
    
    
    def withdraw(self,amount):
        
        if amount < self.balance:
            self.balance = self.balance - amount
            print ("Withdraw Accepted")
            return (f"Your new balance is {self.balance}")
        else:
            print ("Funds Unavailable")


# In[88]:


# 1. Instantiate the class
acct1 = Account('Anindya',400)


# In[89]:


acct1.owner


# In[91]:


acct1.balance


# In[92]:


# 2. Print the object
print(acct1)


# In[93]:


# 5. Make a series of deposits and withdrawals
acct1.deposit(50)


# In[94]:


acct1.withdraw(75)


# In[ ]:




