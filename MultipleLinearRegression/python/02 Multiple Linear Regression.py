
# coding: utf-8

# # Multiple Linear Regression

# ## Car dataset

# In[3]:


# For reading data set
# importing necessary libraries
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt


# In[4]:


# data visualization
get_ipython().run_line_magic('matplotlib', 'inline')


# In[5]:


# filtering of warnings
import warnings
warnings.filterwarnings('ignore')


# In[8]:


# loading the data
cars = pd.read_csv("/home/shashanksoni092/DataScienceWorkspace/DataScienceProjectsPdf/MultipleLinearRegression/python/Cars.csv")


# In[9]:


# checking format of the dataset
type(cars)


# In[12]:


# to get top 5 rows
cars.head(3) # to get top n rows use cars.head(10)


# In[13]:


cars.shape # to see the dimension of dataset


# In[14]:


cars.columns


# In[15]:


# Correlation matrix 
cars.corr() 
# we see there exists High collinearity between input variables especially between
# [Hp & SP] , [VOL,WT] so there exists collinearity problem


# In[11]:


type(cars)


# In[16]:


# Scatter plot between the variables along with histograms
import seaborn as sns


# In[17]:


# pairplot
sns.pairplot(cars.iloc[:,:10])


# In[18]:


# columns names
cars.columns


# In[19]:


# pd.tools.plotting.scatter_matrix(cars); -> also used for plotting all in one graph


# In[18]:


# preparing model considering all the variables 
import statsmodels.formula.api as smf # for regression model


# In[19]:


# Preparing model                  
ml1 = smf.ols('MPG ~ WT + VOL + SP + HP',data=cars).fit() # regression model


# In[20]:


# Getting coefficients of variables               
ml1.params


# In[21]:


# Summary
ml1.summary()
# p-values for WT,VOL are more than 0.05 and also we know that [WT,VOL] has high correlation value


# In[22]:


# preparing model based only on Volume
ml_v=smf.ols('MPG ~ VOL',data = cars).fit()  
ml_v.summary() # 0.271
# p-value <0.05 .. It is significant


# In[23]:


# Preparing model based only on WT
ml_w=smf.ols('MPG ~ WT',data = cars).fit()  
ml_w.summary() # 0.268


# In[24]:


# Preparing model based only on WT & VOL
ml_wv=smf.ols('MPG ~ WT + VOL',data = cars).fit()  
ml_wv.summary() # 0.264


# In[27]:


# Both coefficients p-value became insignificant... 
# So there may be a chance of considering only one among VOL & WT


# In[28]:


# Checking whether data has any influential values 
# influence index plots


# In[25]:


import statsmodels.api as sm
sm.graphics.influence_plot(ml1)
# index 76 AND 78 is showing high influence so we can exclude that entire row


# In[31]:


# Studentized Residuals = Residual/standard deviation of residuals


# In[26]:


# dropping influential records
cars_new = cars.drop(cars.index[[76,70]],axis=0) # ,inplace=False)


# In[29]:


type(cars_new)
cars_new.shape
cars.shape


# In[30]:


# Preparing model                  
ml_new = smf.ols('MPG ~ WT + VOL + HP + SP',data = cars_new).fit()


# In[31]:


# Getting coefficients of variables        
ml_new.params


# In[32]:


# Summary
ml_new.summary() # 0.806


# In[36]:


# Confidence values 99%
print(ml_new.conf_int(0.01)) # 99% confidence level


# In[37]:


# Predicted values of MPG 
mpg_pred = ml_new.predict(cars_new)
mpg_pred


# In[38]:


# view top 5 records in a dataset
cars_new.head()


# In[34]:


rsq_hp = smf.ols('HP ~ WT + VOL + SP',data=cars).fit()
rsq_hp.summary()


# In[38]:


# calculating VIF's values of independent variables
rsq_hp = smf.ols('HP ~ WT + VOL + SP',data=cars).fit().rsquared  
vif_hp = 1/(1-rsq_hp) # 16.33
vif_hp


# In[40]:


rsq_wt = smf.ols('WT ~ HP + VOL + SP',data=cars).fit().rsquared  
vif_wt = 1/(1-rsq_wt) # 564.98
vif_wt


# In[41]:


rsq_vol = smf.ols('VOL ~ WT+SP+HP',data=cars).fit().rsquared  
vif_vol = 1/(1-rsq_vol) #  564.84
vif_vol


# In[42]:


rsq_sp = smf.ols('SP ~WT+VOL+HP',data=cars_new).fit().rsquared  
vif_sp = 1/(1-rsq_sp) #  16.35
vif_sp


# In[43]:


# Storing vif values in a data frame
d1 = {'Variables':['Hp','WT','VOL','SP'],'VIF':[vif_hp,vif_wt,vif_vol,vif_sp]}
Vif_frame = pd.DataFrame(d1)  
Vif_frame
# As weight is having higher VIF value, we are not going to include this prediction model


# In[45]:


# Added varible plot 
sm.graphics.plot_partregress_grid(ml1)


# In[53]:


# added varible plot for weight is not showing any significance 


# In[46]:


# final model
final_ml= smf.ols('MPG ~ VOL + SP + HP',data = cars).fit()
final_ml.params


# In[47]:


# final model summary
final_ml.summary()


# In[56]:


# As we can see that r-squared value has increased from 0.810 to 0.812.


# In[49]:


# prediction using final model
mpg_pred = final_ml.predict(cars)
mpg_pred


# In[58]:


import statsmodels.api as sm


# In[60]:


# added variable plot for the final model
sm.graphics.plot_partregress_grid(final_ml)


# In[62]:


######  Linearity #########
# Observed values VS Fitted values
plt.scatter(cars_new.MPG,mpg_pred,c="r");plt.xlabel("observed_values");plt.ylabel("fitted_values")
plt.show()


# In[63]:


# Residuals VS Fitted Values 
plt.scatter(mpg_pred,final_ml.resid_pearson,c="r")
plt.axhline(y=0,color='blue')
plt.xlabel("fitted_values")
plt.ylabel("residuals")
plt.show()


# In[64]:


########    Normality plot for residuals ######
# histogram
plt.hist(final_ml.resid_pearson) # Checking the standardized residuals are normally distributed
plt.show()


# In[65]:


# QQ plot for residuals 
import pylab          
import scipy.stats as st


# In[67]:


# Checking Residuals are normally distributed
st.probplot(final_ml.resid_pearson, dist="norm", plot=pylab)
plt.show()


# In[69]:


############ Homoscedasticity #######

# Residuals VS Fitted Values 
plt.scatter(mpg_pred,final_ml.resid_pearson,c="r"),plt.axhline(y=0,color='blue')
plt.xlabel("fitted_values")
plt.ylabel("residuals")
plt.show()


# In[71]:


### Splitting the data into train and test data 
from sklearn.model_selection import train_test_split
cars_train, cars_test  = train_test_split(cars_new,test_size = 0.2) # 20% size


# In[72]:


# preparing the model on train data 

model_train = smf.ols("MPG~HP+SP+VOL",data=cars_train).fit()


# In[73]:


# train_data prediction
train_pred = model_train.predict(cars_train)


# In[74]:


# train residual values 
train_resid  = train_pred - cars_train.MPG


# In[75]:


# RMSE value for train data 
train_rmse = np.sqrt(np.mean(train_resid*train_resid))


# In[76]:


# prediction on test data set 
test_pred = model_train.predict(cars_test)


# In[77]:


# test residual values 
test_resid  = test_pred - cars_test.MPG


# In[78]:


# RMSE value for test data 
test_rmse = np.sqrt(np.mean(test_resid*test_resid))

