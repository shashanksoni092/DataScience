#Reading csv file
data<-read.csv("/home/shashanksoni092/DataScienceWorkspace/DataScienceProjectsPdf/Clustering/R/Universities.csv")
View(data)

#Modifying data
data<-data[,2:7]

#Scaling the columns
normalized_data=scale(data)
View(normalized_data)

#Finding the eucledian distance between all the sets or tuples
d<-dist(normalized_data,method="euclidean")
?dist
d

#Applying Hierarchical clustering to the data
fit<-hclust(d,method="complete")
fit


#Plotting the clustering Dendogram 
plot(fit)

?plot
#plotting the model with hang attribute
plot(fit,hang = -1)


#Cutting the Dendogram with 4 clusters
groups<-cutree(fit,k=4)
groups

#Creating rectangle hierarchical clustering model 
rect.hclust(fit,k=4,border="RED")

#Converting the rows into columns ie hrizontal val to vertical val
clustno<-as.data.frame(groups)

#Combining clustno and data
final<-data.frame(clustno,data)
View(final)
attach(final)

#Calling aggregate() to find mean of all the clusters formed
aggregate(final[,3:7],by=list(final$groups),FUN=mean)







