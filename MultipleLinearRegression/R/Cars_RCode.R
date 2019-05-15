
Cars <- read.csv("/home/shashanksoni092/DataScienceWorkspace/DataScienceProjectsPdf/MultipleLinearRegression/R/Cars.csv") # choose the Cars.csv data set
View(Cars)
attach(Cars)
# Exploratory Data Analysis(60% of time)
# 1. Measures of Central Tendency
# 2. Measures of Dispersion
# 3. Third Moment Business decision
# 4. Fourth Moment Business decision
# 5. Probability distributions of variables
# 6. Graphical representations
  #  > Histogram,Box plot,Dot plot,Stem & Leaf plot, 
  #     Bar plot

summary(Cars)

# 7. Find the correlation b/n Output (MPG) & (HP,VOL,SP)-Scatter plot
pairs(Cars)

# 8. Correlation Coefficient matrix - Strength & Direction of Correlation
cor(Cars)

# The Linear Model of interest
model.car <- lm(MPG ~ VOL + HP + SP + WT,data=Cars)

summary(model.car)

# Prediction based on only Volume 
model.carV <-lm(MPG ~ VOL)
summary(model.carV) # Volume became significant

# Prediction based on only Weight
model.carW<-lm(MPG~WT)
summary(model.carW) # Weight became significant

# Prediction based on Volume and Weight
model.carVW <- lm(MPG~VOL+WT)
summary(model.carVW) # Both became Insignificant

# It is Better to delete influential observations rather than deleting entire column which is 
# costliest process
# Deletion Diagnostics for identifying influential observations
influence.measures(model.car)
library(car)
## plotting Influential measures
#windows()
influenceIndexPlot(model.car) # index plots for infuence measures
influencePlot(model.car) # A user friendly representation of the above

# Regression after deleting the 77th observation, which is influential observation
model.car1 <- lm(MPG ~ VOL + SP + HP + WT,data=Cars[-77,])
summary(model.car1)

# Regression after deleting the 77th & 71st Observations
model.car2 <- lm(MPG~VOL+SP+HP+WT,data=Cars[-c(71,77),])
summary(model.car2)

## Variance Inflation factor to check collinearity b/n variables 
vif(model.car)
## vif>10 then there exists collinearity among all the variables 

## Added Variable plot to check correlation b/n variables and o/p variable
#windows()
avPlots(model.car)

## VIF and AV plot has given us an indication to delete "wt" variable

## Final model
finalmodel <- lm(MPG ~ VOL+SP+HP)
summary(finalmodel)

# Evaluate model LINE assumptions 
plot(finalmodel)
windows()
#Residual plots,QQplot,std-Residuals Vs Fitted,Cook's Distance 
qqPlot(model.car,id.n = 5)
# QQ plot of studentized residuals helps in identifying outlier 

library(MASS)
stepAIC(model.car)
