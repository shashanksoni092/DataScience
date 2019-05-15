install.packages("plyr")

data<-read.csv("/home/shashanksoni092/DataScienceWorkspace/DataScienceProjectsPdf/Clustering/R/Universities.csv")
View(data)

normalized_data<-scale(data[,2:7])
normalized_data
?kmeans
ml<-kmeans(normalized_data,5)

str(ml)
cluster<-ml$cluster
cluster

mlfinal<-data.frame(normalized_data,cluster)
mlfinal
  