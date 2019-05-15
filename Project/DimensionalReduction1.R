#Predicting GradRate using PCA

data<-read.csv("/home/shashanksoni092/DataScienceWorkspace/DataScienceProjectsPdf/Project/dataset/Universities.csv")
View(data)

help("princomp")

#Removing 1st column
data<-data[-1]

#Correlation
cor(data)

#Summary of data
summary(data)


#Implementing a PCA model using princomp()
pca<-princomp(data,cor=TRUE)

#Gives a summar of pca model
summary(pca)

#Weights of pca Columns
loadings(pca)

#pca model description with 7 sublist 
str(pca)

#Plot ie bar plot of variances of pca columns 
plot(pca)

#Displaying all pca columns
pca$scores

data<-cbind(data,pca$scores[,1:2])
View(data)

#Eliminating redundant columns
new_data<-data[,6:8]
View(new_data)
attach(new_data)

#Apply linear regression to calculate Gradrate
lm1<-lm(GradRate~Comp.1+Comp.2,data=new_data)
summary(lm1)

#86.15% accuracy



data<-cbind(data,pca$scores[,1:6])
View(data)

#Eliminating redundant columns
new_data<-data[,6:14]
View(new_data)
attach(new_data)

lm2<-lm(GradRate~Comp.1+Comp.2+Comp.3+Comp.4+Comp.5+Comp.6,data=new_data)
summary(lm2)


help("predict")
library("MASS")
stepAIC(lm2)













