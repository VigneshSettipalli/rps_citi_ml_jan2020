# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 14:20:23 2020

@author: Balasubramaniam
"""

class ClaimOfficer(object):  # -> don't forget the object specified as base
    
    '''
    def __new__(cls,id,name,age,email):
        print ("A.__new__ called")
        return super(ClaimOfficer, cls).__new__(cls)
    '''
    #static variable
    message=""    
    #private variables are __
    def __init__(self,id,name,age,email):
        print ("Customer.__init__ called")
        self.__id=id
        self.__name=name
        self.__age=age
        self.__email=email
        
    def setId(self,value):
        self.__id=value
        
    def getId(self):
        return self.__id
    
    def getEmail(self):
        return self.__email
    
    @staticmethod
    def validateEmail(email):
        
        if (email.find("@") != -1):
            ClaimOfficer.message="Valid"
        else:
            ClaimOfficer.message="invalid"
        return ClaimOfficer.message
        
        
'''    
claimOfficer=ClaimOfficer(3274576,'Ajay',45,'ajay@gmail.com')
print("Before update=%d" %(claimOfficer.getId()))
claimOfficer.setId(324858)
print("After update=%d" %(claimOfficer.getId()))
#invoke static method
print(ClaimOfficer.validateEmail(claimOfficer.getEmail()))
'''


