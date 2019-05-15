







#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Created on Fri Oct 26 19:10:47 2018

#@author: shashanksoni092
#"""


data=read.csv("/home/shashanksoni092/DataScienceWorkspace/DataScienceProjectsPdf/Project/dataset/Universities.csv")
data

?drop
#Dropping Univ column
data<-data[,2:7]




ml1<-lm('GradRate~SAT+Top10+Accept+SFRatio+Expenses',data=data)
summary(ml1)
library("MASS")
stepAIC(ml1)
#Correlation
data.corr()

#SAT-Top10,SAT-Accept,Top10-Accept are highly correlated
#Building a linear model

ml1=smf.ols('GradRate~SAT+Top10+Accept+SFRatio+Expenses',data=data).fit()
ml1.params
ml1.summary()
#No column is significant

#SAT-Top10,SAT-Accept,Top10-Accept are highly correlated

ml2=smf.ols('GradRate~SAT+Top10',data=data).fit()
ml2.params
ml2.summary()
#Sat and Top10 both are not significant

ml3=smf.ols('GradRate~SAT+Accept',data=data).fit()
ml3.params
ml3.summary()
#Accept is significant

ml4=smf.ols('GradRate~Accept+Top10',data=data).fit()
ml4.params
ml4.summary()
#Accept is significant

ml5=smf.ols('GradRate~Top10+Accept+SFRatio+Expenses',data=data).fit()
ml5.params
ml5.summary()
#Accept is significant


# dropping influential records
#data_new = data.drop(data.index[[17,19]],axis=0) # ,inplace=False)
#but since we alredy have less rows so it wont be good to delete a tuple 


#calculating the vif's of all the columns(variance influencial factor)
#vif has to be claculated manually
#vif(x)=1/(1-rsq(x))  

#vif of SAT
rsq_SAT=smf.ols('SAT~Top10+Accept+SFRatio+Expenses',data=data).fit().rsquared
vif_SAT=1/(1-rsq_SAT)
vif_SAT


#vif of Top10
rsq_Top10=smf.ols('Top10~SAT+Accept+SFRatio+Expenses',data=data).fit().rsquared
vif_Top10=1/(1-rsq_Top10)
vif_Top10


#vif of Accept
rsq_Accept=smf.ols('Accept~Top10+SAT+SFRatio+Expenses',data=data).fit().rsquared
vif_Accept=1/(1-rsq_Accept)
vif_Accept

#vif of SFRatio
rsq_SFRatio=smf.ols('SFRatio~Top10+Accept+SAT+Expenses',data=data).fit().rsquared
vif_SFRatio=1/(1-rsq_SFRatio)
vif_SFRatio

#vif of Expenses
rsq_Expenses=smf.ols('Expenses~Top10+Accept+SAT+SFRatio',data=data).fit().rsquared
vif_Expenses=1/(1-rsq_Expenses)
vif_Expenses

#storing vif in a dataframe
d1 = {'Variables':['SAT','Top10','Accept','SFRatio','Expenses'],'VIF':[vif_SAT,vif_Top10,vif_Accept,vif_SFRatio,vif_Expenses]}
Vif_frame = pd.DataFrame(d1)  
Vif_frame


# As SAT is having higher VIF value, we are not going to  include it in our model 
ml6=smf.ols('GradRate~Top10+Accept+SFRatio+Expenses',data=data).fit()
ml6.params
ml6.summary()
#Accept is significant

# As Top10 is having higher VIF value, we are not going to  include it in our model 
ml7=smf.ols('GradRate~Accept+SFRatio+Expenses',data=data).fit()
ml7.params
ml7.summary()
#Accept is significant

# As Top10 is having higher VIF value, we are not going to  include it in our model 
ml8=smf.ols('GradRate~Accept+SFRatio',data=data).fit()
ml8.params
ml8.summary()
#Accept is significant


