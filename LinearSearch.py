#!/usr/bin/env python
# coding: utf-8

# In[5]:


def linearsearch(dataset, value):
    for index, val in enumerate(dataset):
        if value == val:
            return index
    else:
        return None


# In[6]:


dataset = [1,2,3]
value = 2
linearsearch(dataset, value)


# In[ ]:




