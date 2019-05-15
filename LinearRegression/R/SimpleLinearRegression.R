#Linear Regression
##Simple Linear Regression
###Author:-SHASHANK SONI

```{r}
data<-read.csv("/home/shashanksoni092/DataScienceWorkspace/DataScienceProjectsPdf/LinearRegression/wc-at.csv")
dim(data)
View(data)
attach(data)
plot(Waist,AT)#To scatter the points ie, a scatterplot
# Correlation coefficient value for Waist and FAT Data
cor(AT,Waist)
cor(Waist,AT)
class(data)#To know the datatype of data
#To know the structure of the data
str(data)
#to know the standard deviation of waist
sd(Waist)

#To get the summary of the data(Business Decision)
summary(data)

#Time to create a LinearModel for the data

#Syntax for that is lm(y~x)
model1<-lm(AT~Waist)
summary(model1)
confint(model1,level = 0.95)
predict(model1)
predict(model1,interval="predict")
# R-squared value for the above model is 0.667. 
# we may have to do transformation of variables for better R-squared value
# Applying transformations

# Logarthmic transformation
reg_log <- lm(AT ~ log(Waist))  # Regression using logarthmic transformation
summary(reg_log)
confint(reg_log,level=0.95)
predict(reg_log,interval="predict")
# R-squared value for the above model is 0.6723. 
# we may have to do different transformation better R-squared value
# Applying different transformations

# Exponential model 
reg_exp<-lm(log(AT) ~ (sqrt(Waist*Waist*Waist))) # regression using Exponential model
summary(reg_exp)
# R-squared value has increased from 0.67 to 0.7071 
# Higher the R-sqaured value - Better chances of getting good model 
# for Waist and addipose Tissue







```