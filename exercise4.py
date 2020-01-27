# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 12:24:02 2020

@author: Balasubramaniam
"""
#dictionary
import datetime
vehicleDictionary={"regNo":"TN-32-AE-01234","color":"Blue",
                   "regDate":datetime.date(2020,1,2),
                   "make":"Hyundai"}
#print all the keys
for key in vehicleDictionary.keys():
    print(key)
  
#print all the values
for value in vehicleDictionary.values():
    print(value)   
    
#key and value

for(key,value) in vehicleDictionary.items():
    print(key,"==>",value)
    
 
import requests

response=requests.get("https://jsonplaceholder.typicode.com/users") 
#print(response.json())

for user in response.json():
    for (key,value) in user.items():
         if(key=="name"):
           print(value,"=>",end="\t")
         if(key=="email"):
           print(value,end="\n") 
    
response=requests.get("https://www.quandl.com/api/v3/datasets/AMFI/134014.json?api_key=nHYufVSHw4383Wy4_Ekg")
'''
for i in range(0,7):
    print(response.json()["dataset"]["data"][i])
'''    
for data in response.json()["dataset"]["data"]:
    print(data)
    
    
    
    
    
    

