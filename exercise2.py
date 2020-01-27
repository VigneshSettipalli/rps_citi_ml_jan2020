# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 11:35:33 2020

@author: Balasubramaniam
"""

#conditoinal statements
import random
genData=random.randint(1,100000)
print(genData)

if (genData<1000):
    print("Data lies below 1000 --> %d" %(genData))
elif (genData>1000) and (genData <10000):
    print("Data lies between 1001 to 9999 --> %d" %(genData))
else:
    print("Data above 9999 --> %d" %(genData))
    
    
print(1000<=genData<=10000)

#loops

for _ in range(1,100):
    print(random.randint(1,10000))



    



    
    
    
    
    
    
    
    
    
    
    