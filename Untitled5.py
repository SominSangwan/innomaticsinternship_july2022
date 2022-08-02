#!/usr/bin/env python
# coding: utf-8

# In[1]:


my_string = "Hello, World!"
print(my_string)


# In[7]:


n = int(input())
if n%2 == 1:
    print("Weird")
elif n%2 ==0 and 2<= n <=5:
    print("Not Weird")
elif n%2 ==0 and 6<=n <=20:
    print("Weird")
else:
    print("Not Weird") 


# In[8]:


n = int(input())
if n%2 == 1:
    print("Weird")
elif n%2 ==0 and 2<= n <=5:
    print("Not Weird")
elif n%2 ==0 and 6<=n <=20:
    print("Weird")
else:
    print("Not Weird") 


# In[10]:


a = 3
b = 2
print(a+b)
print(a-b)
print(a*b)


# In[11]:


a=4
b=3
print(a//b)
print(a/b)


# In[28]:


n = int(input())
for i in range(0,n):
 print(i*i)


# In[29]:


def is_leap(year):
    leap = False
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False
    
    
    
    return leap


# In[30]:


year = int(input())
print(is_leap(year))


# In[31]:


if __name__ == '__main__':
    n = int(input())
    for i in range (1,n+1):
        print(i,end='')


# In[ ]:




