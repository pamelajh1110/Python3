#!/usr/bin/env python
# coding: utf-8

# In[3]:


def bubblesort(li):
    n = len(li)
    for i in range(0, n-1):
        for j in range(0, n-i-1):
            if all(li[j] <= li[j+1] for j in range(0, n-i-1)):
                return li
            elif li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
        print(li)
    return li


# In[4]:


li = [1, 2, 3 ,4, 6, 7, 5]
bubblesort(li)


# In[ ]:




