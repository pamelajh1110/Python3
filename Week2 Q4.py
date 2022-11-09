#!/usr/bin/env python
# coding: utf-8

# In[13]:


def LCM(a,b):
    if a*b == 0:
        h = 0
    else:
        c = max(a,b)
        d = min(a,b)
        e = c%d
        while e!=0:
            g = d%e
            d = e
            e = g
        h = int((a*b)/d)
    return h

if __name__ == '__main__':
    #a = int(input())
    #b = int(input())
    a,b = map(int, input().split())
    print(LCM(a,b))


# 

# In[ ]:




