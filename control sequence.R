#control statements in R
#install.packages("dplyr")
library("dplyr")
a=as.integer(readline("enter age"))
print(a)
cat("hello",a)
#fibbonacci
i=as.integer(readline("n:"))
f=c(0,1)
sum=1
for(x in 3:i)
{f[x]=f[x-1]+f[x-2]
 sum=sum+f[x]

 }
cat("sum is",sum,"series is",f)
