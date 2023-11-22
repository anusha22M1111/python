#lepto(1-0.25) meso(-0.25-0.25) platy(-0.23--1)
#outliers
#range, iqr, mean median,sd,varience,cov,skew,kutorsis
rm(list=ls()) #removes unwanted variables

library(MASS)
n=na.omit(geyser)
#View(n)
d=n$duration
mean(d)
median(d)
quantile(d,c(.58))
IQR(d)
var(d)
sd(d)
#install.packages("e1071")
library(e1071)
moment(d,order=3,center=TRUE)
skewness(d)
kurtosis(d)


