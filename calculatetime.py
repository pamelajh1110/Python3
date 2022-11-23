#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time

def calculatetime(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print("%s running time: %s secs." % (func.__name__, t2 - t1))
        return result

    return wrapper


# In[ ]:




