#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 20:19:44 2018

@author: shashanksoni092
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 19:10:47 2018

@author: shashanksoni092
"""


#Exploring the data and importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv("/home/shashanksoni092/DataScienceWorkspace/DataScienceProjectsPdf/Project/dataset/Universities.csv")
data

#Dropping Univ column
data.drop(["Univ"],axis=1,inplace=True)

#seaborn is used to plot statistical plot
import seaborn as sb

data.columns
sb.boxplot(x="SAT",data=data)
sb.boxplot(x="Top10",data=data)
sb.boxplot(x="Accept",data=data)
sb.boxplot(x="SFRatio",data=data)
sb.boxplot(x="GradRate",data=data)

#Checking null values
data.isnull().sum()

#Contains no null value

data.columns
#Building a statsmodel

import statsmodels.formula.api as smf 


#Correlation
data.corr()

#SAT-Top10,SAT-Accept,Top10-Accept are highly correlated
#Building a linear model

ml1=smf.ols('Expenses~SAT+Top10+Accept+SFRatio+GradRate',data=data).fit()
ml1.params
ml1.summary()
#SAT column is significant

#SAT-Top10,SAT-Accept,Top10-Accept are highly correlated

ml2=smf.ols('Expenses~SAT+Top10',data=data).fit()
ml2.params
ml2.summary()
#Sat and Top10 both are significant

ml3=smf.ols('Expenses~SAT+Accept',data=data).fit()
ml3.params
ml3.summary()
#Accept and SAT are significant

ml4=smf.ols('Expenses~Accept+Top10',data=data).fit()
ml4.params
ml4.summary()
#nothing is significant

ml5=smf.ols('Expenses~Top10+SAT+SFRatio+GradRate',data=data).fit()
ml5.params
ml5.summary()
#SAT is significant


# dropping influential records
#data_new = data.drop(data.index[[17,19]],axis=0) # ,inplace=False)
#but since we alredy have less rows so it wont be good to delete a tuple 


#calculating the vif's of all the columns(variance influencial factor)
#vif has to be claculated manually
#vif(x)=1/(1-rsq(x))  

#vif of SAT
rsq_SAT=smf.ols('SAT~Top10+Accept+SFRatio+GradRate',data=data).fit().rsquared
vif_SAT=1/(1-rsq_SAT)
vif_SAT


#vif of Top10
rsq_Top10=smf.ols('Top10~SAT+Accept+SFRatio+GradRate',data=data).fit().rsquared
vif_Top10=1/(1-rsq_Top10)
vif_Top10


#vif of Accept
rsq_Accept=smf.ols('Accept~Top10+SAT+SFRatio+GradRate',data=data).fit().rsquared
vif_Accept=1/(1-rsq_Accept)
vif_Accept

#vif of SFRatio
rsq_SFRatio=smf.ols('SFRatio~Top10+Accept+SAT+GradRate',data=data).fit().rsquared
vif_SFRatio=1/(1-rsq_SFRatio)
vif_SFRatio

#vif of GradRate
rsq_GradRate=smf.ols('GradRate~Top10+Accept+SAT+SFRatio',data=data).fit().rsquared
vif_GradRate=1/(1-rsq_GradRate)
vif_GradRate

#storing vif in a dataframe
d1 = {'Variables':['SAT','Top10','Accept','SFRatio','GradRate'],'VIF':[vif_SAT,vif_Top10,vif_Accept,vif_SFRatio,vif_GradRate]}
Vif_frame = pd.DataFrame(d1)  
Vif_frame


# As SAT is having higher VIF value, we are not going to  include it in our model 
ml6=smf.ols('Expenses~Top10+Accept+SFRatio+GradRate',data=data).fit()
ml6.params
ml6.summary()
#SFRatio is significant

# As Top10 is having higher VIF value, we are not going to  include it in our model 
ml7=smf.ols('Expenses~Accept+SFRatio+GradRate',data=data).fit()
ml7.params
ml7.summary()
#SFRatio is significant

# As SFRatio is having higher VIF value, we are not going to  include it in our model 
ml8=smf.ols('Expenses~SAT+SFRatio',data=data).fit()
ml8.params
ml8.summary()
#Accept is significant

# As Expenses is having higher VIF value, we are not going to  include it in our model 
ml9=smf.ols('Expenses~SFRatio+SAT+GradRate',data=data).fit()
ml9.params
ml9.summary()
#Accept is significant

prediction=ml9.predict(data)

final_data=pd.concat([data,prediction],axis=1)


#65.7% accuracy
