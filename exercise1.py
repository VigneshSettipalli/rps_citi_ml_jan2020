# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 09:42:22 2020

@author: Balasubramaniam
"""
print("Training is on Machine Learning using Python and R")
#identifier
'''
firstName=input("Enter First Name")
lastName=input("Enter Last Name")
age=int(input("Enter Age"))
#data type
print(type(age))
#show the result
print("Customer First Name=%s\n Last Name=%s\n Age=%d" %(firstName,lastName,age))
'''
#complex number
print(complex(5,25))
dob=input("Enter DOB(yyyy-mm-dd)")
print("DOB=%s" %(dob))
dobarr=dob.split("-")
print(dobarr[0],dobarr[1],dobarr[2])
#convert string to date
import datetime
customerDOB=datetime.date(int(dobarr[0]),int(dobarr[1]),int(dobarr[2]))
print(customerDOB)
print(type(customerDOB))
#format the date
print(customerDOB.strftime("%d/%m/%Y"))















