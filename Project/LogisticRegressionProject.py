#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 17:19:26 2018

@author: shashanksoni092
"""

#Exploring the data and importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv("/home/shashanksoni092/DataScienceWorkspace/DataScienceProjectsPdf/Project/dataset/mtcars.csv")
data

data.head()

import seaborn as sb

#Plots
sb.boxplot(x="mpg",data=data)

sb.countplot(x="am",data=data)

sb.boxplot(x="mpg",y="disp",data=data,palette="hls")
sb.boxplot(x="mpg",y="disp",data=data)

sb.boxplot(x="mpg",y="wt",data=data,palette="hls")

sb.boxplot(x="hp",y="disp",data=data,palette="hls")

#correlation
data.corr()

#correlation plots
sb.pairplot(data)

#Checking null values
data.isnull().sum()

data.drop(['car_model'],axis=1,inplace=True)
data.drop(['cyl','drat','vs','gear','carb','qsec'],axis=1,inplace=True)
data
data.iloc[:,:]=data.iloc[:,:].apply(lambda a :a.fillna(a.mean()))

#Checking null values
data.isnull().sum()


#Splitting into training and testing data
Y=data["am"]
data.drop("am",axis=1,inplace=True)
X=data

#importing train_test_split from sklearn.cross_validation
from sklearn.cross_validation import train_test_split

#Dividng data into x_train,x_test,y_train,y_test
x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2)

from sklearn.linear_model import LogisticRegression
logit=LogisticRegression()

#Fitting a model
logit.fit(x_train,y_train)

#Printing the logarithmic coefficient
logit.coef_

#Printing the actual coefficient
np.exp(logit.coef_)


#Predicting the value for x_test
predictions=logit.predict(x_test)

#Calculating the accuracy through ClassificationReport
from sklearn.metrics import classification_report

classification_report(y_test,predictions)

#Calculating the accuracy through ConfusionMatrix

from sklearn.metrics import confusion_matrix

confusion_matrix(y_test,predictions)
accuracy = sum(y_test==predictions)/data.shape[0]
accuracy

#Caculating accuracy
from sklearn.metrics import accuracy_score
accuracy_score(y_test,predictions)






#Since,we have only 32 records so it wont be good to divide  data into training and testing data and hence test_size=0

#Dividng data into x_train,x_test,y_train,y_test
x_train1,x_test1,y_train1,y_test1=train_test_split(X,Y,test_size=0)

from sklearn.linear_model import LogisticRegression
logit=LogisticRegression()

#Fitting a model
logit.fit(x_train,y_train)

#Printing the logarithmic coefficient
logit.coef_

#Printing the actual coefficient
np.exp(logit.coef_)


#Predicting the value for x_test
predictions=logit.predict(x_train1)

#Calculating the accuracy through ClassificationReport
from sklearn.metrics import classification_report

classification_report(y_train1,predictions)

#Calculating the accuracy through ConfusionMatrix

from sklearn.metrics import confusion_matrix

confusion_matrix(y_train1,predictions)
accuracy = sum(y_train1==predictions)/data.shape[0]
accuracy

#Caculating accuracy
from sklearn.metrics import accuracy_score
accuracy_score(y_train1,predictions)
#Accuracy 81.25





