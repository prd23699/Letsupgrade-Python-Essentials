#!/usr/bin/env python
# coding: utf-8

# # Loop Example
# #Prime number
# 

# In[2]:


for num in range(1,200):
    for i in range(2,num):
        if (num % i) == 0:
            break
    else:
            print(num)


# In[ ]:




