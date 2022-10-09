#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Problem 1 - Define a function called myfunc that takes an arbitrary number of arguments, and returns a list 
#containing only those arguments that are even.


# In[2]:


def myfunc(*args):
    out = []
    for num in args:
        if num%2 == 0:
            out.append(num)
    return out


# In[3]:


myfunc(3,9,4,7,10,48,21,37,48)


# In[4]:


#Problem 2 - Define a function that takes in a string, and returns a matching string where every even letter is
#uppercase, and every odd letter is lowercase. 


# In[16]:


def myfunc(word):
    out = []
    for index,letter in enumerate(word):
        if index%2 == 0:
            out.append(letter.upper())
        else:
            out.append(letter.lower())
    
    return ''.join(out)


# In[17]:


myfunc('JuxtaPOSED')


# In[18]:


myfunc('PythonSuperhero')


# In[7]:


#Problem 3 - LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers *if* both numbers are 
#even, but returns the greater if one or both numbers are odd.


# In[2]:


def lesser_of_two_even(a,b):
    if a%2 == 0 and b%2 == 0:
        if a>b:
            return b
        else:
            return a
    if a%2 == 1 or b%2 == 1:
        if a>b:
            return a
        else:
            return b


# In[3]:


lesser_of_two_even(2,4)


# In[4]:


lesser_of_two_even(75,77)


# In[5]:


lesser_of_two_even(74,37)


# In[2]:


#Better way to solve it
def lesser_of_two_even(a,b):
    if a%2 == 0 and b%2 == 0:
        return min(a,b)
    else:
        return max(a,b)


# In[3]:


lesser_of_two_even(2,4)


# In[4]:


lesser_of_two_even(75,77)


# In[5]:


lesser_of_two_even(74,37)


# In[12]:


#Problem 4 - ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with 
#same letter


# In[6]:


def two_word_string(x):
    mystring = x.lower().split()
    #used lower function in case anyword start with lowercase so to make sure it does not return false
    #could have use upper function to make all word uppper case as well
    if mystring[0][0] == mystring[1][0]:
        return True
    else:
        return False


# In[7]:


two_word_string('Levelheaded Llama')


# In[8]:


two_word_string('Crazy Kangaroo')


# In[10]:


two_word_string('Crazy cangaroo')


# In[16]:


# Problem 5 - MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 *or* if one of the 
#integers is 20. If not, return False.


# In[17]:


def makes_twenty(a,b):
    if a+b == 20:
        if a or b == 20:
            return True
    else:
        return False


# In[18]:


makes_twenty(15,5)


# In[19]:


makes_twenty(20,0)


# In[20]:


makes_twenty(1,5)


# In[12]:


#Better solution
def makes_twenty(a,b):
    return a+b == 20 or a == 0 or b == 20
#since it is a boolean check, it can be done in one line


# In[13]:


makes_twenty(15,5)


# In[14]:


makes_twenty(20,0)


# In[15]:


makes_twenty(1,5)


# In[21]:


# Problem 6 - OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
# old_macdonald('macdonald') --> MacDonald


# In[19]:


def myfunc(word):
    out = []
    for index,letter in enumerate(word):
        if (index == 0) or (index == 3):
                out.append(letter.upper())
        else:
            out.append(letter.lower())
    
    return ''.join(out)


# In[20]:


myfunc('macdonald')


# In[22]:


myfunc('anindya')


# In[16]:


#Alternate way to solve it
def myfunc(name):
    first_half = name[:3]
    second_half = name[3:]
    
    return first_half.capitalize() + second_half.capitalize()


# In[17]:


myfunc('macdonald')


# In[18]:


myfunc('anindya')


# In[24]:


#Alternate way to solve it
def myfunc(name):
    first_half = name[:3]
    second_half = name[3:]
    
    return first_half.capitalize() + second_half.capitalize()
def myfunc(x):
    out = []
    for i in range(len(x)):
        if (i==0) or (i==3):
            out.append(x[i].upper())
        else:
            out.append(x[i].lower())
    return ''.join(out)


# In[25]:


myfunc('macdonald')


# In[30]:


# Problem 7 - MASTER YODA: Given a sentence, return a sentence with the words reversed


# In[20]:


def MASTER_YODA(x):
    out = []
    mystring = x.split()[::-1]
    for item in mystring:
        out.append(item)
    return ' '.join(out)


# In[21]:


MASTER_YODA('I am learning python')


# In[33]:


# Problem 8 - ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200


# In[23]:


def almost_there(n):
    if abs(100-n) <= 10 or abs(200-n) <= 10:
        return True
    else:
        return False


# In[24]:


almost_there(89)


# In[25]:


almost_there(96)


# In[26]:


almost_there(185)


# In[27]:


almost_there(195)


# In[28]:


almost_there(205)


# In[22]:


#Better solution
def almost_there(n):
    return abs(100-n) <= 10 or abs(200-n) <= 10


# In[29]:


almost_there(89)


# In[40]:


# Problem 9 - FIND33 - Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
#use .sort and .count, think about in function as well#hoyni


# In[19]:


def has_33(x):
    for i in range(0,len(x)-1):
        if x[i] == 3 and x[i+1] == 3:
            return True
    else:
        return False


# In[14]:


has_33([1, 3, 3])


# In[20]:


has_33([1, 3, 1, 3])


# In[18]:


has_33([3, 3, 1])


# In[21]:


has_33([4, 1, 5])


# In[46]:


#Problem 10 - PAPER DOLL: Given a string, return a string where for every character in the original there are three characters


# In[47]:


def paper_doll(x):
    out = []
    for i in x:
        out.append(3*i)
    return ''.join(out)


# In[48]:


paper_doll('Hello')


# In[49]:


paper_doll('Mississippi')


# In[50]:


# Problem 11 - BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. 
# If their sum exceeds 21 *and* there's an eleven, reduce the total sum by 10. Finally, if the sum (even after 
# adjustment) exceeds 21, return 'BUST'


# In[51]:


def blackjack(a,b,c):
    if a+b+c <= 21:
        return a+b+c
    elif a==11 or b==11 or c ==11 and a+b+c-10<21:
        return a+b+c-10
    elif a+b+c >21:
        return 'BUST'


# In[52]:


blackjack(5,6,7)


# In[53]:


blackjack(9,9,9)


# In[54]:


blackjack(9,9,11)


# In[23]:


#### Problem 12 - SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 
#and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.


# In[ ]:


#think about how to summer_69([6,9, 5, 6, 7, 8, 9])


# In[6]:


def summer_69(nums):
    total = 0
    add = True
    
    for i in nums:
        while add:
            if i != 6:
                total = total + i
                break
            else:
                add = False
        while add == False:
            if i != 9:
                break
            else:
                add = True
                break
    return total


# In[2]:


summer_69([6,9, 5, 6, 7, 8, 9])


# In[3]:


summer_69([4, 5, 13, 6, 7, 8, 9])


# In[4]:


summer_69([6, 2,3,9,4, 5, 13, 6, 7, 8, 9])


# In[64]:


#Problem 13 - SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order


# In[1]:


def spy_game(nums):
    for i in range(len(nums)):
        if nums[i] == 0:
            for x in range(len(nums)):
                if i<x and nums[x] == 0:
                    for y in range(len(nums)):
                        if x<y and nums[y] == 7:
                            return True
    else:
        return False


# In[2]:


spy_game([1,3,7,2,0,4,5,0])


# In[28]:


spy_game([1,0,2,4,0,5,7])


# In[3]:


spy_game([1,2,4,0,0,7,5,3])


# In[4]:


spy_game([0,2,0,4,0,2,5,7])


# In[5]:


spy_game([1,2,6,4,3,0,0,7])


# In[6]:


spy_game([1,2,6,4,3,0,7,0])


# In[2]:


#Alternate way to do it
def spy_game(nums):
    code = [0,0,7,'X']
    for i in nums:
        if i == code[0]:
            code.pop(0)
    return len(code) == 1


# In[3]:


spy_game([1,3,7,2,0,4,5,0])


# In[4]:


spy_game([1,0,2,4,0,5,7])


# In[5]:


spy_game([1,2,4,0,0,7,5,3])


# In[6]:


spy_game([0,2,0,4,0,2,5,7])


# In[7]:


spy_game([1,2,6,4,3,0,0,7])


# In[8]:


spy_game([1,2,6,4,3,0,7,0])


# In[9]:


#Problem 14 - COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given 
#number


# In[1]:


def count_primes(n):
    if n<2:
        return 0
    #check to avoid 0 and 1
    
    prime = [2]
    # to deal with number > 2
    
    x = 3
    while x <= n:
        for i in range(3,x,2):
            if x%i == 0:
                x+=2
                break
        else:
            prime.append(x)
            x +=2
    return len(prime)


# In[2]:


count_primes(100)


# In[ ]:


# Problem 15 - PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter


# In[1]:


def print_big(letter):
    patterns = {1:'  *  ',2:' * * ',3:'*   *',4:'*****',5:'**** ',6:'   * ',7:' *   ',8:'*  * ',9:'*    '}
    alphabet = {'A':[1,2,4,3,3], 'B':[5,3,5,3,5], 'C':[4,9,9,9,4], 'D':[5,3,3,3,5], 'E':[4,9,5,9,4]}
    for pattern in alphabet[letter.upper()]:
        print (patterns[pattern])


# In[2]:


print_big('A')


# In[ ]:


# Problem 16 - Write a function that computes the volume of a sphere given its radius.
#The volume of a sphere is given as (4/3)*π*r^3


# In[3]:


def vol(rad):
    volume = 4/3*22/7*rad**3
    return volume


# In[4]:


vol(2)


# In[5]:


# Problem 17 - Write a function that checks whether a number is in a given range (inclusive of high and low)


# In[25]:


def ran_check(num,low,high):
    if num in range(low,high):
        print (f'{num} is in the range {low} and {high}')


# In[26]:


ran_check(5,2,7)


# In[27]:


# Problem 18 - Return a boolean that checks whether a number is in a given range (inclusive of high and low)


# In[93]:


def ran_bool(num,low,high):
    if num in range(low,high + 1):
        return True
    else:
        return False


# In[94]:


ran_bool(5,2,7)


# In[95]:


ran_bool(2,5,7)


# In[35]:


#Problem 19 - Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.**

#   Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
#   Expected Output : 
#   No. of Upper case characters : 4
#   No. of Lower case Characters : 33

#   HINT: Two string methods that might prove useful: **.isupper()** and **.islower()**
#   If you feel ambitious, explore the Collections module to solve this problem!


# In[38]:


def up_low(s):
    upper = 0
    lower = 0
    for letter in s:
        if letter.isupper():
            upper = upper + 1
        if letter.islower():
            lower = lower + 1
    print (f'No. of Upper case characters : {upper}')
    print (f'No. of Lower case characters : {lower}')


# In[39]:


up_low('Hello Mr. Rogers, how are you this fine Tuesday?')


# In[40]:


#Problem 20 - Write a Python function that takes a list and returns a new list with unique elements of the first list.

#Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
#Unique List : [1, 2, 3, 4, 5]


# In[43]:


def unique_list(lst):
    return list(set(lst))


# In[44]:


unique_list([1,1,1,1,2,2,3,3,3,3,4,5])


# In[45]:


# Problem 21 - Write a Python function to multiply all the numbers in a list.


# In[49]:


def multiply(numbers):
    import math
    return math.prod(numbers)


# In[53]:


multiply([1,2,3,-4])


# In[96]:


#Alternate way
def multiply(numbers):
    total = 1
    for num in numbers:
        total = total*num
    return total


# In[97]:


multiply([1,2,3,-4])


# In[54]:


# Problem 22 - Write a Python function that checks whether a word or phrase is palindrome or not.


# In[65]:


def palindrome(s):
    if s.replace(' ','') == s.replace(' ','')[::-1]:
        return True
    else:
        return False


# In[66]:


palindrome('madam')


# In[67]:


palindrome('nurses run')


# In[68]:


import string
string.ascii_lowercase


# In[91]:


import string
def ispangram(str1, alphabet=string.ascii_lowercase):
    if set(str1.replace(' ','').lower()) == set(alphabet):
        return True
    else:
        return False


# In[92]:


ispangram("The quick brown fox jumps over the lazy dog")


# In[90]:


str1 = "The quick brown fox jumps over the lazy dog"
(set(str1.replace(' ','').lower()))

