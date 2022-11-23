#!/usr/bin/env python
# coding: utf-8

# In[8]:


def BinarySearch(data, value):
    n = len(data)
    left = 0
    right = n-1
    while left < right:
        mid = (right + left) //2
        if data[mid] == value:
            return mid
        elif data[mid] < value:
            left = mid
        else:
            right = mid
    else:
        return None


# In[9]:


dataset = [1,3,5,7,8,9,10]
value = 3
BinarySearch(dataset, value)

