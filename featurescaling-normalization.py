# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 06:05:10 2018

@author: Balasubramaniam
"""
import pandas as pd
# Age vector
age = (25, 35, 50)
# Salary vector
salary = (200000, 1200000, 2000000)
# Data frame created using age and salary
df = pd.DataFrame( {"Age":age, "Salary":salary})
print(df)

from sklearn import preprocessing
x = df.values #returns a numpy array
#print(x)
min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(x)
df = pd.DataFrame(x_scaled)
print(df)







