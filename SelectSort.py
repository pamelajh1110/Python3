#!/usr/bin/env python
# coding: utf-8

# In[1]:


def selectsort(li):
    n = len(li)
    for i in range(n-1):
        for j in range(n-i-1):
            if li[i] > li[i+j+1]:
                li[i], li[i+j+1] = li[i+j+1], li[i]
    return li


# In[2]:


li = [1, 2, 3 ,4, 6, 7, 5]
selectsort(li)

