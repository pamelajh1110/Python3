#!/usr/bin/env python
# coding: utf-8

# In[39]:


def GCD(a,b):
    if a*b == 0:
        d = max(a, b)
    else:
        c = max(a,b)
        d = min(a,b)
        e = c%d
        while e!=0:
            g = d%e
            d = e
            e = g
    return d

if __name__ == '__main__':
    #a = int(input())
    #b = int(input())
    a,b = map(int, input().split())
    print(GCD(a,b))
    


# 

# In[ ]:




