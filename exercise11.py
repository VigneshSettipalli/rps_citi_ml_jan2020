# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 16:47:49 2020

@author: Balasubramaniam
"""
import pymysql
import os
path="G:/Local disk/citi_ml_jan2020/backup/user.csv"

userColl=[]
def getData():
    if(os.path.exists(path)):
       print("file exists")
       fileRef=open(path,'r')
       for line in fileRef:
           print(line)
           userColl.append(line.split(","))           
    else:
        print("File not exists")
    return userColl    

def createConnection():
    connection=pymysql.connect(host="localhost",user="root",
                    passwd="vignesh",db="citimljan20db")

    return connection


def addUser(data):
    conn=createConnection()
    cursor=conn.cursor()
    try:
       cursor.execute("""insert into citi_user values('%s','%s','%s')"""
                      %(data[0],data[1],data[2])) 
       conn.commit()
    except pymysql.Error as err:
        print("Exception occurred",err)
        conn.rollback()
    finally:
        conn.close()
    
def deleteAllUsers():
    conn=createConnection()
    cursor=conn.cursor()
    try:
       cursor.execute("""delete from citi_user""") 
       conn.commit()
    except pymysql.Error as err:
        print("Exception occurred",err)
        conn.rollback()
    finally:
        conn.close()
    
 
deleteAllUsers()
    
for user in getData():
     addUser(user)
    
    
    
    
    
    
    
    
    
    


