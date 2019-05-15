#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 21:42:50 2018

@author: shashanksoni092
"""

import pandas as pd
import numpy as np
import matplotlib.pylab as plt

data=pd.read_csv("/home/shashanksoni092/DataScienceWorkspace/DataScienceProjectsPdf/Project/dataset/mtcars.csv")
data

#Slicing the dataframe 
data=data.iloc[:,1:8]
data

#sum of all the null values for each column
data.isnull().sum()

#using lambda function to replace null values with mean value
data.apply(lambda a:a.mean())

#sum of all the null values for each column
data.isnull().sum()

#filling the null value with mean value of each column
data.iloc[:,0:8]=data.iloc[:,0:8].apply(lambda x:x.fillna(x.mean()))

#sum of all the null values for each column
data.isnull().sum()

#null values are successfully eliminated

#Checking the correlation between columns
datacorr=data.corr()
#cyl-disp disp-wt are highly correlated

import seaborn as sns
#seaborn is used to plot scatterplot between different columns along with histogram

#pairplot
sns.pairplot(data)
#%matplotlib auto


# preparing model considering all the variables 
import statsmodels.formula.api as smf # for regression model

#creating a linear model
ml1=smf.ols('mpg~cyl+disp+hp+drat+wt+qsec',data=data).fit()

#Coefficients:-
ml1.params
    
#summary of model
ml1.summary()
#only wt is significant and rest all are not

import statsmodels.api as sm
sm.graphics.influence_plot(ml1) 

# dropping influential records
#data_new = data.drop(data.index[[17,19]],axis=0) # ,inplace=False)
#but since we alredy have less rows so it wont be good to delete a tuple 

#calculating the vif's of all the columns(variance influencial factor)
#vif has to be claculated manually
#vif(x)=1/(1-rsq(x))  

#vif of cyl
rsq_cyl=smf.ols('cyl~disp+hp+drat+wt+qsec',data=data).fit().rsquared
vif_cyl=1/(1-rsq_cyl)
vif_cyl

#vif of disp
rsq_disp=smf.ols('disp~cyl+hp+drat+wt+qsec',data=data).fit().rsquared
vif_disp=1/(1-rsq_disp)
vif_disp

#vif of hp
rsq_hp=smf.ols('hp~cyl+disp+drat+wt+qsec',data=data).fit().rsquared
vif_hp=1/(1-rsq_hp)
vif_hp

#vif of drat
rsq_drat=smf.ols('drat~cyl+disp+hp+wt+qsec',data=data).fit().rsquared
vif_drat=1/(1-rsq_drat)
vif_drat

#vif of qsec
rsq_qsec=smf.ols('qsec~cyl+disp+hp+wt+drat',data=data).fit().rsquared
vif_qsec=1/(1-rsq_qsec)
vif_qsec

#vif of wt
rsq_wt=smf.ols('wt~cyl+disp+hp+qsec+drat',data=data).fit().rsquared
vif_wt=1/(1-rsq_wt)
vif_wt

#storing vif in a dataframe
d1 = {'Variables':['cyl','disp','hp','drat','qsec','wt'],'VIF':[vif_cyl,vif_disp,vif_hp,vif_drat,vif_qsec,vif_wt]}
Vif_frame = pd.DataFrame(d1)  
Vif_frame
# As disp is having higher VIF value, we are not going to  include it in our model 

# Added varible plot 
sm.graphics.plot_partregress_grid(ml1)

ml2=smf.ols('mpg~cyl+hp+drat+qsec+wt',data=data).fit()
ml2.params
ml2.summary()


#storing vif in a dataframe
d1 = {'Variables':['cyl','hp','drat','qsec','wt'],'VIF':[vif_cyl,vif_hp,vif_drat,vif_qsec,vif_wt]}
Vif_frame = pd.DataFrame(d1)  
Vif_frame
# As cyl is having higher VIF value, we are not going to  include it in our model 

ml3=smf.ols('mpg~hp+drat+qsec+wt',data=data).fit()
ml3.params
ml3.summary()

#Rsquared value is increased by a slight  norm
#moreover qsec and wt both have become significant


#storing vif in a dataframe
d1 = {'Variables':['hp','drat','qsec','wt'],'VIF':[vif_hp,vif_drat,vif_qsec,vif_wt]}
Vif_frame = pd.DataFrame(d1)  
Vif_frame
# As wt is having higher VIF value, we are not going to  include it in our model 

ml4=smf.ols('mpg~hp+drat+qsec',data=data).fit()
ml4.params
ml4.summary()

#storing vif in a dataframe
d1 = {'Variables':['hp','drat','qsec'],'VIF':[vif_hp,vif_drat,vif_qsec]}
Vif_frame = pd.DataFrame(d1)  
Vif_frame
# As hp is having higher VIF value, we are not going to  include it in our model 


ml5=smf.ols('mpg~drat+qsec',data=data).fit()
ml5.params
ml5.summary()


#we observed  that ml3 has more r_squared value than ml4 and ml5

#Hence going back to ml3 and further improvise it in different direction

ml3=smf.ols('mpg~hp+drat+qsec+wt',data=data).fit()
ml3.params
ml3.summary()

#Lets remove hp

ml6=smf.ols('mpg~drat+qsec+wt',data=data).fit()
ml6.params
ml6.summary()

ml7=smf.ols('mpg~qsec+wt',data=data).fit()
ml7.params
ml7.summary()

# ml7 is  better model than all till this point

#But lets go back to ml3 ,
ml3=smf.ols('mpg~hp+drat+qsec+wt',data=data).fit()
ml3.params
ml3.summary()

#removing drat this time
ml8=smf.ols('mpg~hp+qsec+wt',data=data).fit()
ml8.params
ml8.summary()


# ml7 is  better model than all till this point hence improving it by using transformation

ml8=smf.ols('np.log(mpg)~qsec+wt',data=data).fit()
ml8.params
ml8.summary()


ml9=smf.ols('np.log(mpg)~np.log(qsec)+wt',data=data).fit()
ml9.params
ml9.summary()


#86.4 accuracy
mpg_prediction=ml9.predict(data)
mpg_prediction

ml7=smf.ols('mpg~qsec+wt',data=data).fit()
ml7.params
ml7.summary()

mpg_prediction2=ml7.predict(data)
mpg_prediction2

new_data=pd.concat([data,mpg_prediction2],axis=1)
new_data

######  Linearity #########
# Observed values VS Fitted values

plt.scatter(data.mpg,mpg_prediction2,c="r");plt.xlabel("observed_values");plt.ylabel("fitted_values")
plt.show()

