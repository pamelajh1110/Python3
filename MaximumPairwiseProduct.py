#Goal: Maximum Pairwise Product
#Requirement: Working in less than one second even on huge datasets
#!/usr/bin/env python
# coding: utf-8

# In[54]:


import numpy as np
def fibonacci(n):
    fib = []
    #l = []
    if n == 0:
        fib = [0]
    elif n == 1:
        fib = [0,1]
    else:
        fib = [0,1]
        for i in range(2,n+1):
            a = fib[i-1] + fib[i-2]
            l = len(str(a))
            b = str(a)[l-1:l]
            fib.append(int(b))
    return int(fib[n])

if __name__ == '__main__':
    n = int(input())
    print(fibonacci(n))




