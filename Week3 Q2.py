#!/usr/bin/env python
# coding: utf-8

# In[1]:


def maxcost(n, r, a, b):
    #a = [a0, a1,a2, a3, ... ,an-1]
    #b = [b0, b1, b2, b3, ... ,bn-1]
    c = []
    for i in range(0, n):
        c.append(a[i]/b[i])
    #print(c)
    
    Addre = 0
    if sum(b) < r:
        return sum(a)
    else:
        while r > 0:
            ck = max(c)
            k = c.index(ck)
            if b[k] >= r:
                Addre += r * c[k]
                r = 0
            else:
                Addre += b[k] * c[k]
                r = r - b[k]
                c[k] = 0
                
    
    
    Addre = '%.4f' % Addre
    return Addre

if __name__ == '__main__':
    #_ = int(input())
    p,q = list(map(int, input().split()))
    a = []
    b = []
    #a,b = list(map(int, input().split()))
    for i in range(0,p):
        m,n = list(map(int, input().split()))
        a.append(m)
        b.append(n)
        
    print(maxcost(p,q,a,b))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




