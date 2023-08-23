#practice test2
#22mia1111

#q1-dna sequence
str=input()
a=str.count('A')
g=str.count('G')
c=str.count('C')
t=str.count('T')
d={'A':a,'G':g,'C':c,'T':t}
print(d)

#q-2
str="have a good day!"
'''print(str[0])
a=str.split(" ")
for i in range(len(a)):
   a[i].replace(((a[i])[0]),((a[i])[0]).upper())
print(a)
.replace()
'''
a=str.title()
print(a)

#q-3 customer rating
n=int(input())
l1=[]
l2=[]
l=[[input() for j in range(3)] for i in range(n)]
for i in range(n):
    if int(l[i][1])<=20:
        l1.append(l[i])
    else:
        l2.append(l[i])
print(l)
print(l1)
print(l2)
#q-4
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
m=int(input())
n=int(input())
print(gcd(m,n)) 

#question_5
def punc(a):
    res=""
    pun=".,?';:[{(!-)}]"
    for x in a:
        if x not in pun:
            res+=x
    return(res)
str=input()
b=punc(str)
print(b)
#question_6:
 #class_10
#question_7:
f1=open("D:\mtech-cse-ba\fall-2023-24\file.csv","r")
fcontent=f1.readlines()
f2 =open("D:\mtech-cse-ba\fall-2023-24\result.csv","w")
f2.writelines(fcontent)
f2.close()
f1.close()
