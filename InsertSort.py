#!/usr/bin/env python
# coding: utf-8

# In[6]:


def insertsort(li):
    n = len(li)
    for i in range(1,n):
        tmp = li[i]
        j = i - 1
        while li[j] > tmp and j >= 0:
            li[j + 1] = li[j]
            li[j] = tmp
            j = j - 1
    return li
            


# In[7]:


li = [1, 2, 5, 3, 7, 2, 5]
insertsort(li)


# In[ ]:




