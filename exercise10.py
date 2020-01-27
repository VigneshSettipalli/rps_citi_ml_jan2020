# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 16:39:57 2020

@author: Balasubramaniam
"""

import os
path="G:/Local disk/course content"
count=0
for(path,dirnames,filenames) in os.walk(path):
    for file in filenames:
        print(file)
        (shortname,extension) = os.path.splitext(file)
        print(extension)
        if(extension==".docx"):
           count=count+1
           
print("Total Word File Count %d" %(count))