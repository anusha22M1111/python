df1=data.frame(id=c(1,2,3),name=c('aa','bb','cc'),marks=c(22,33,44))
#View(df1)
df1
str(df1)
a=class(df1)
a
b=typeof(df1)
b
c=nrow(df1)
c
d=ncol(df1)
d
e=dim(df1)
e
summary(df1)
#basic operations in dataframe
colnames(df1)
head(df1,2)
tail(df1,2)
df1$name
df1[c(1,3),]
df1$age=c(21,23,24)
df1
df1=rbind(df1,c(4,"dd ",79,25))

#in csv
#   write.csv(df,nameoffile.csv,row.names = FALSE)
#example-1
d=data.frame(name=c('aa','bb','cc','dd','ee'),e1=c(1,2,3,4,5),e2=c(4,5,6,7,8),e3=c(3,5,7,9,1),e4=c(2,4,6,8,0))
d
#View(d)
d[c(2,3),]
d$e4
total=d[,c(2:5)]
total
d1=rowSums(total)
d$total=d1
d

d$name[which.max(d$total)]
d2=c("avg",mean(d$e1),mean(d$e2),mean(d$e3),mean(d$e4),mean(d$total))
d=rbind(d,d2)
d
write.csv(d,'df_exm.csv',row.names = FALSE)
