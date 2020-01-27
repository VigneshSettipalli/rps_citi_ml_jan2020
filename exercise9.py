# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 15:29:27 2020

@author: Balasubramaniam
"""

#read json write to csv file

import os
import requests
response=requests.get("https://jsonplaceholder.typicode.com/users")
userColl=[]
for user in response.json():
    userData=[]
    for (key,value) in user.items():
         if(key=="name"):
           #print(value,"=>",end="\t")
           userData.append(value)
         if(key=="email"):
           #print(value,"=>",end="\t") 
           userData.append(value)
         if(key=="phone"):
           #print(value,end="\n")
           userData.append(value)
    userColl.append(userData)  
    
print(userColl)   
    
path="G:/Local disk/citi_ml_jan2020/"

header=["Name","Email","Phone"]
if(os.path.exists(path+"/backup")):
    print("dir exists")
    if(os.path.exists(path+"/backup/user.csv")):
        print("File Exists")
        fileRef=open(path+"/backup/user.csv",'w')
        for heading in header:
            fileRef.write(heading+",")
        fileRef.write("\n")
        
        for user in userColl:
            for item in user:
               fileRef.write(item+",")
            fileRef.write("\n")   
        fileRef.close()
    else:
        print("File Not Existing")
        open(path+"/backup/user.csv",'w')
        print("File Created")     
else:
    print("not exist")
    dir=os.mkdir(path+"/backup")
    print("directory created")
    
    
    
    
    
    
    
    
    
    
    
    