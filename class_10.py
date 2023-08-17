#class_10
#22mia1111

#eg:1

def add(a,b):
    tot=a+b
    avg=tot/2
    return(tot,avg)
x=int(input())
y=int(input())
t=add(x,y)
print(t)

#example 2:write a function to sort a list with n numbers and print the sorted 
#list along with the average
l=[]
n=int(input())
for i in range(n):
    l=l+[int(input())]

def sa(a):
    a.sort()
    avg=sum(a)/len(a)
    return(a,avg)

b,c=sa(l)
print(b)
print(c)

#notes
def func(*t)--       #passing values as tuples
tot=t[0]+t[1]+t[2]   #accessing values in tuple

def func(**t)--      #passing values as dictionary
func(a=10,b=20,c=30)
tot=t[a]+t[b]+t[c]   #accessing values in dictionary

#find factorial of number using recursion

a=int(input())    #4
def fac(t):
    if t==0:
        return 1
    else:
        return t*fac(t-1)
print(fac(a))  ---#ans:24

#write a recursive fuction to calculate the gcd of two numbers

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
print(gcd(100,60)) ----#ans:20

#lambda function
lambda arguments :expression  #many arguments but only 1 expression


#example:
x=lambda a:a+10
print(x(20))  ----#ans:30

#example using if else:
maxnum=lambda a,b: a if a>b else b
print(maxnum(20,10))


#legb rules
l=local function
e=enclosing function
g=global scope
b=built in modules

import math
x1=5
x2=15
x3=20
y1=10
y2=20
y3=15

def linear(x1,y1,x2,y2,x3,y3):
    if(x1==x2==x3 or y1==y2==y3):
        return 0
    else:
        return 1

def dist(x1,y1,x2,y2):
    a=math.pow(x1-x2,2)
    b=math.pow(y1-y2,2)
    dis=math.sqrt(a+b)
    return(dis)

def chec(x1,y1,x2,y2,x3,y3):
    if dist(x1,y1,x2,y2)+dist(x2,y2,x3,y3)>dist(x1,y1,x3,y3):
        return 1
    elif dist(x1,y1,x2,y2)+dist(x1,y1,x3,y3)>dist(x2,y2,x3,y3):
        return 1
    elif dist(x2,y2,x3,y3)+dist(x1,y1,x3,y3)>dist(x1,y1,x2,y2):
        return 1
    else:
        return 0

def fin(x1,y1,x2,y2,x3,y3):
    if linear(x1,y1,x2,y2,x3,y3)>0 and chec(x1,y1,x2,y2,x3,y3)>0:
        print("yes")
    else:
        print("No")
      
fin(x1,y1,x2,y2,x3,y3)















