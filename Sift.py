#!/usr/bin/env python
# coding: utf-8

# In[34]:


def sift(li):
    low = 0
    high = len(li) - 1
    
    i = 0 #堆顶
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
        
        
    
        
        
    
    


# In[35]:


li = [2, 7, 5, 3, 4, 1]
sift(li)


# In[ ]:




