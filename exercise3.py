# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 11:49:18 2020

@author: Balasubramaniam
"""

#List
customer=['Ashok','Kumar',2465645,True]
for _ in customer:
    print(_)
    
customers=[['Ashok','Kumar',2465645,True],
           ['Abhishek','Rawat',2465646,False],
           ['Ritu','Kumari',2465648,True],
           ['Anoop','Chauhan',2465649,True]]    


#print only customer id
pos=int(input("Data to search"))
for cust in customers:
    print(cust[pos],end="\t")
    for data in cust: 
        if(type(data)==int):
            print(data)
       
 #concatenation
orgList=["TCS","CITI","HSBC"]
locList=["Chennai","Pune","Hyderabad"]
print(orgList+locList)       
#ordered list concat        
for (org,loc) in zip(orgList,locList):
    print(org,"-->",loc)        
        
#append the data
orgList.append("Fiserv")
print(orgList)        
#assignment     
locList[0]="Bangalore"
print(locList)


#tuple
gender=("MALE","FEMALE","TRANSGENDER")
print(gender)        
#append the data
#gender.append("Unknown")        
#print(gender)  

#gender[0]="UnKnown"
#print(gender)  
        
        
employees=[('Ashok','Kumar',2465645,True),
           ('Abhishek','Rawat',2465646,False),
           ('Ritu','Kumari',2465648,True),
           ('Anoop','Chauhan',2465649,True)]          
        
employees.append(('Shyam','Kumar',24656488,False)) 
       
members=(['Ashok','Kumar',2465645,True],
           ['Abhishek','Rawat',2465646,False],
           ['Ritu','Kumari',2465648,True],
           ['Anoop','Chauhan',2465649,True])
import datetime   
members[0].append(datetime.date(1999,12,12))
    






