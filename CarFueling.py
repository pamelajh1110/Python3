#Car Fueling
#Compute the minimum number of gas tank refills to get from one city to another.

#Input: Integers d and m, as well as a sequence of integers stop1 < stop2 < ··· < stopn.
#Output: The minimum number of refills to get from one city to another if a car can travel at most m miles on a full tank.
#The distance between the cities is d miles and there are gas stations at distances stop1,stop2,...,stopn along the way.
#We assume that a car starts with a full tank.

#Input format: The first line contains an integer d. The second line contains an integer m. The third line specifies an integer n.
#Finally, the last line contains integers stop1,stop2,...,stopn.

#Output format: The minimum number of refills needed. If it is not possi- ble to reach the destination, output −1.

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


#Sample:
#Input:
#950
#400
#4
#200 375 550 750
#Output:
#2


    
# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




