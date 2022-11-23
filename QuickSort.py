#!/usr/bin/env python
# coding: utf-8

# In[82]:


def quickpar(li, i, j):
    #n = len(li)
    tmp = li[i]
    #i = 0
    #j = n - 1
    while i < j:
        while li[j] >= tmp and i < j:
            j = j - 1
        
        li[i] = li[j]
        while li[i] <= tmp and i < j:
            i = i + 1
        
        li[j] = li[i]
        
    li[i] = tmp
    return i
    
def quicksort(li,i,j):
    if i<j:
        mid = quickpar(li, i, j)
        quicksort(li, i, mid-1)
        quicksort(li, mid+1, j)
    return li
        


# In[83]:


lists = [5.5, 2, 7, 3, 5, 7, 4, 8, 5]
i = 0
j = 8
quicksort(lists,0,8)

