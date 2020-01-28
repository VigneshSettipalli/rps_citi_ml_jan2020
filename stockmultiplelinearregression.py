# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 14:26:39 2018

@author: Balasubramaniam
"""
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import sklearn

dataset = pd.read_csv('MSFT.csv')
X = dataset.iloc[:, 1:4].values
y = dataset.iloc[:, 5:6].values
print(X,y)
print(X.shape)
print(y.shape)

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=sklearn.model_selection.train_test_split(X,y,test_size=0.13,random_state=2)


from sklearn.linear_model import LinearRegression

lm=LinearRegression()
result=lm.fit(X_train,Y_train)

import statsmodels.api as sm

est = sm.OLS(Y_train, X_train) #ordinary least square method 
est2 = est.fit()
print("Summary.....")
print(est2.summary())


#LinearRegression(copy_X=True, fit_intercept=True, normalize=False)
print("Estimated intercept coefficient",lm.intercept_)
print("coefficients",lm.coef_)
plt.scatter(X[:,1],y)
plt.plot(X[:,1],y,'g.')
plt.xlabel("Open Stock")
plt.ylabel("Closing Stock")
plt.title("Relationship between Open and Close Stock")
plt.show()
plt.scatter(X[:,2],y)
plt.xlabel("Low Stock")
plt.ylabel("Closing Stock")
plt.title("Relationship between Low and Close Stock")
plt.show()

#predicting stock price
print(lm.predict(X)[0:5])
plt.scatter(X[:,2],lm.predict(X))
plt.plot(X[:,1],lm.predict(X), 'k.') #color code is k or m or etc.,
plt.xlabel("Low")
plt.ylabel("Predicted Close")
plt.title("Low vs Closing Price")
plt.show()
#Mean Sqaured Error
MSE=np.mean((y-lm.predict(X))**2)
print("Mean Sqaured Error %r" %(MSE))
#Sum of Sqaured Error
SSE=np.sum((y-lm.predict(X))**2)
print("SUM of Sqaured Error %r" %(SSE))



#training and test data set
'''
X_train,X_test,Y_train,Y_test=sklearn.model_selection.train_test_split(X,bos.PRICE,test_size=0.13,random_state=2)
print('X train shape','-->',X_train.shape)
print('X test shape','-->',X_test.shape)
print(Y_train.shape)
#print(Y_test.shape)
lm=LinearRegression()
lm.fit(X_train,Y_train)
pred_train=lm.predict(X_train)
pred_test=lm.predict(X_test)
print("Estimated intercept coefficient",lm.intercept_)
print("Number of coefficients",len(lm.coef_))
print ("Fit a model X_train, and calculate MSE with Y_train:" , np.mean((Y_train-lm.predict(X_train)) ** 2))
print ("Fit a model X_train, and calculate MSE with Y_test:" , np.mean((Y_test-lm.predict(X_test)) ** 2))
'''