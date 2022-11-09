#Maximum Value of the Loot (Fractional Knapsack)

#Maximizing the Value of the Loot Problem
#Find the maximal value of items that fit into the backpack.

#Input: The capacity of a back- pack W as well as the weights (w1,...,wn) and costs (c1,...,cn) of n different compounds.
#Output: The maximum total value of fractions of items that fit into the backpack of the given capacity:
#i.e., the maximum value of c1 ·f1 +· · ·+cn · fn such that w1 ·f1 +···+wn ·fn ≤ W and 0≤fi ≤1 for all i
#(fi is the fraction of the i-th item taken to the backpack).

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


    
#Input:
3 50
60 20
100 50
120 30

#Output:
180.0000

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




