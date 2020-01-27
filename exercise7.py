# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 15:11:01 2020

@author: Balasubramaniam
"""
import sys
sys.path.append("./")
from exercise6 import ClaimOfficer
#inheritance
class ClaimAuthorizer(ClaimOfficer):    
    def __init__(self,id,name,age,email,limit):
        
        ClaimOfficer.__init__(self,id,name,age,email)
        self.limit=limit
        
claimAuthorizer=ClaimAuthorizer(358789,'Julie',35,'julie@gmail.com',500000)
print(claimAuthorizer.getId())