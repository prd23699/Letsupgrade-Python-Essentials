#!/usr/bin/env python
# coding: utf-8

# # List

# In[5]:


lst=["pavan",30,54,34.50,27,"rokade",[3,4,5]]


# In[6]:


lst


# In[7]:


lst.append(9)


# In[4]:


lst


# In[8]:


lst[4]


# In[9]:


lst[1:3]


# In[10]:


lst[-2]


# In[11]:


lst[-2][1]


# In[12]:


lst.insert(2,45)


# In[13]:


lst


# In[14]:


lst.pop()


# In[15]:


lst


# In[16]:


lst.reverse()


# In[17]:


lst


# In[18]:


lst.index(30)


# In[19]:


lst.remove(45)
lst


# In[20]:


lst.extend([4,6,8])
lst


# In[21]:


lst.insert(3,"Hii")
lst


# In[22]:


lst1 = lst.copy()
lst1


# In[23]:


lst1.clear()
lst1


# In[26]:


lst.count(27)


# In[27]:


lst1=[2,7,3,5,9]
lst1.sort()


# In[28]:


lst1


# # Dictionary

# In[40]:


dic={"Name":"Pavan","Age":21,"Number":2356783450,"Villege":"Malkapur"}


# In[41]:


dic


# In[42]:


dic.get("Name")


# In[43]:


dic.items()


# In[44]:


dic.pop("Name")


# In[45]:


dic


# In[46]:


dic["city"]="Buldhana"


# In[47]:


dic


# In[48]:


dic.keys()


# In[49]:


dic.popitem()


# In[50]:


dic


# In[51]:


dic1={"Age":22}


# In[52]:


dic.update(dic1)


# In[53]:


dic


# In[54]:


dic.values()


# # Sets

# In[55]:


st={1,4,2,8,6,7,3,9,5,3,7,4,7,9,3}


# In[56]:


st


# In[57]:


st.add(10)


# In[58]:


st


# In[59]:


st1={2,4,3,6,8,4,6,9,5}
st1


# In[60]:


st1.issubset(st)


# In[61]:


st.update([11,12,1,2])


# In[62]:


st


# In[63]:


st.discard(12)
st


# In[64]:


st.remove(11)
st


# In[65]:


st.pop()
st


# In[66]:


st.union(st1)


# In[67]:


st.intersection(st1)


# In[68]:


st.difference(st1)


# In[69]:


st.symmetric_difference(st1)


# In[70]:


st.isdisjoint(st1)


# In[71]:


st.issuperset(st1)


# In[72]:


st.update()


# In[73]:


st


# In[74]:


st.difference_update()
st


# In[76]:


st.intersection_update()
st


# # String
# 

# In[78]:


name = "pavan"
name


# In[79]:


name1 = "rokade"
name1


# In[80]:


name+name1


# In[81]:


name.capitalize()


# In[85]:


name.upper()


# In[86]:


name1.isupper()


# In[88]:


name.count(name1)


# In[ ]:




