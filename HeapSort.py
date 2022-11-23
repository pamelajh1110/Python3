#!/usr/bin/env python
# coding: utf-8

# In[11]:


def sift(li, low, high):
    #low = 0
    #high = len(li) - 1
    
    i = low #堆顶
    j = 2 * i + 1 #左孩子
    tmp = li[0]
    
    i = 0 #堆顶
    
    while j <= high:
        
        #if li[j] < li[j + 1]:
            #用j和tmp比
        if j + 1 <= high and li[j] < li[j + 1]:
            j = j + 1
        
        if tmp < li[j]:
            li[i] = li[j]
            i = j
            j = 2 * i + 1 #左孩子
            
        else:
            li[i] = tmp
            print(li)
            break
        
    else:
        li[i] = tmp
        return li

def heapsort(li):
    low = 0
    high = len(li) - 1
    n = len(li)
    for i in range((n-1)//2, -1, -1):
        sift(li, i, high)
    
    for i in range(n-1, -1, -1):
        li[0], li[i] = li[i], li[0]
        sift(li, 0, i - 1)
        
    return li
        
    
    


# In[12]:


li = [2, 3, 5, 7, 4, 1]
heapsort(li)


# In[ ]:




