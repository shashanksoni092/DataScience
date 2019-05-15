
wc.at <- read.csv(file.choose()) # choose the wc-at.csv data set
dim(wc.at)
x <- read.csv("E:\\Excelr DS\\R _Codes\\Simple Linear Regression\\wc-at.csv")
View(wc.at)
var(Waist)
attach(wc.at)
attach(claimants)
windows()
plot(Waist,AT)
# Correlation coefficient value for Waist and FAT Data
cor(AT,Waist)
cor(Waist,AT)
dim(wc.at)
class(wc.at)
str(wc.at)
summary(wc.at)
sd(Waist)
model1 <- lm(AT ~ Waist)
summary(model1)
confint(model1,level = 0.95)
predict(model1,interval="predict")
# R-squared value for the above model is 0.667. 
# we may have to do transformation of variables for better R-squared value
# Applying transformations

# Logarthmic transformation
reg_log <- lm(AT ~ log(Waist))  # Regression using logarthmic transformation
summary(reg_log)
confint(reg_log,level=0.95)
predict(reg_log,interval="predict",newdata = x )
# R-squared value for the above model is 0.6723. 
# we may have to do different transformation better R-squared value
# Applying different transformations

# Exponential model 
reg_exp<-lm(log(AT) ~ (sqrt(Waist*Waist*Waist))) # regression using Exponential model
summary(reg_exp)
# R-squared value has increased from 0.67 to 0.7071 
# Higher the R-sqaured value - Better chances of getting good model 
# for Waist and addipose Tissue
