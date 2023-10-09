#22mia1111
#l-1
#matrix

#matrix(data,rows,columns)
m=matrix(c(1,2,3,4),2,2)
m
a=matrix(c(2,3,4,5),2,2,byrow=TRUE)
a
Rownames=c('aa','bb','cc')
Colnames=c('aa','bb','cc')
y=matrix(20:9,3,3,dimnames = list(Rownames,Colnames))
y
#matrix addition and subtraction
c=a+m
d=a-m
c
d

#mul by scalar
e=3*m
e
#matrix multiplication
f=a%*%m
f

#transpose of matrix
at=t(a)
at

#unit mat
u=matrix(1,3,3)
u
z=matrix(0,3,3)
z
#identity mat
dg=diag(a)
dg

#column or row sums,means
cc=colSums(a)
cc
r=rowSums(a)
r
cm=colMeans(a)
cm
rm=rowMeans(a)
rm
mn=mean(a)
mn

#appending rows or columns
cb=cbind(a,m)
cb
rb=rbind(a,m)
rb

h=matrix(1:12,4,3)
h
j=h[3,2]
j
ar=h[2,]
ar
ac=h[,3]
al=h[,c(1,3)]
ac
al
ht=t(h)
ht
hc=cbind(h,1:4)
hc
hr=rowMeans(h)
hcm=colMeans(h)
hr
hcm
hr[2]
hcm[2]

#list
#creating list of vectors
v1=c(1,2,3)
v2=c('aa','bb')
l=list(v1,v2)
l
#indexing
l[[1]][2]
l[[2]][1]

#defining a namelist
l1=list(marks=1:10,names=v2)
l1

#example-1 of list
le=list(regno=1:2,name=v2,noc=3:4,marks=c(11,67,89,56,80))
le
le1=le[[1]]
le11=le[[4]]
le2=le[[2]][1]
le3=le[[4]][1]
le[[4]][5]=5+le[[4]][5]
le1
le11
le2
le3
le
