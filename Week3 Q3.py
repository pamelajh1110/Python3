#!/usr/bin/env python
# coding: utf-8

# In[1]:


def refill(dis, perfill, ns, s):
    p = []
    d2 = []
    t = [0]
    for i in range(0,ns):
        t.append(s[i])
    t.append(dis)
    #print(t)
    
    for q in range(0,ns+1):
         d2.append(t[q+1]-t[q])
    
    if all(_ <= perfill for _ in d2):      
                
        d = perfill
        for a in range(0, ns+1):
            if t[a+1] > d and t[a] <= d:
                p.append(a)
                d = perfill+t[a]
                #print(d)
        p = len(p)
    else:
            p = -1
            
    return p
        
if __name__ == '__main__':
    #_ = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    
    d = list(map(int, input().split()))
        
    print(refill(a,b,c,d))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




