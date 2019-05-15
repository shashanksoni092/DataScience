#LinearRegresson model where we have to find mpg value after clustering

data<-read.csv("/home/shashanksoni092/DataScienceWorkspace/DataScienceProjectsPdf/Project/dataset/mtcars.csv")
View(data)

#Selecting only important attributes
dataset<-data[,2:8]
View(dataset)

#Searching for values or column which contains null values
col1<- mapply(anyNA,dataset) # apply function anyNA() on all columns of airquality dataset
col1

#Filling the null values
for(i in 1:ncol(dataset)){
  dataset[is.na(dataset[,i]), i] <- mean(dataset[,i], na.rm = TRUE)
}

View(dataset)
  
#Scalling the columns values
normalized_data<-scale(dataset)
View(normalized_data)

?kmeans

# Initialize total within sum of squares error: wss
wss <- 0

# For 1 to 15 cluster centers
for (i in 1:15) {
  km.out <- kmeans(normalized_data, centers = i, nstart = 20)
  # Save total within sum of squares to wss variable
  wss[i] <- km.out$tot.withinss
}

# Plot total within sum of squares vs. number of clusters
plot(1:15, wss, type = "b", 
     xlab = "Number of Clusters", 
     ylab = "Within groups sum of squares")

#we got k=2

ml<-kmeans(normalized_data,2)

str(ml)
cluster<-ml$cluster
cluster
cluster<-as.data.frame(cluster)
View(cluster)

dataset<-data.frame(dataset,cluster)
View(dataset)
#Now ,its time to apply Linear Regession where mpg is output  and rest all are input
mdata<-dataset[,1:7]
View(mdata)

#Plot between different columns
pairs(mdata)

#Correlation between different columns
cor(mdata)

summary(mdata)
#creating a linear model
model.mtcars<-lm(mpg~cyl + disp + hp + drat + wt + qsec,data=mdata)  
summary(model.mtcars)

#cyl-disp , disp-wt are strongly correlated
attach(mdata)
cor(cyl,disp)
cor(disp,wt)

# install.packages("MASS")
library(MASS)
stepAIC(model.mtcars)

#displaying influence points
influence.measures(model.mtcars)

#But since we have very less tuples so its better to eliminate columns rather than tuples

#so we have to check correlation between different columns
library(carData)
library(mvinfluence)
#Variance infuential factor vif is the term for that
vif(model.mtcars)

avPlots(model.car)






