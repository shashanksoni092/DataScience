#Predicting Expenses using PCA

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

data<-cbind(data,pca$scores[,1:3])
View(data)

#Eliminating redundant columns
new_data<-data[,-c(1,2,4,6)]
View(new_data)
attach(new_data)
#Apply linear regression to calculate Accept rate
lm1<-lm(Accept~Comp.1+Comp.2+Comp.3,data=new_data)
summary(lm1)
#90.67% accuracy


#Apply linear regression to calculate Expenses
lm2<-lm(Expenses~Comp.1+Comp.2+Comp.3,data=new_data)
summary(lm2)
#92.56% accuracy
















