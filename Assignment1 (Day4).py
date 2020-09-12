#!/usr/bin/env python
# coding: utf-8

# # ArmStrong Number
# ArmStrong number between 1042000,702648265

# In[ ]:


n = 1042000
while n<= 702648265:
    sum = 0
    temp = n
    while temp>0:
        digit = temp%10
        sum = sum+ digit**3
        temp = temp//10
    if n == sum:
        print(n)
        break
    n = n+1

