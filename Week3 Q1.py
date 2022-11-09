#!/usr/bin/env python
# coding: utf-8

# In[11]:


def Monchange(a):
    if 0 <= a < 5:
        b = a
    elif 5 <= a < 10:
        c = a%5
        b = 1+c
    else:
        d = a%10
        e = (a-d)/10
        g = d%5
        h = (d-g)/5
        b = e+h+g
    return int(b)

if __name__ == '__main__':
    a = int(input())
    print(Monchange(a))


# In[ ]:





# In[ ]:




