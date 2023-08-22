#class_12
#22mia1111
'''
#class
class classname:
    statement-1
    .
    .
    .
    statement-2
class __init__() ----constructor

#example
class complex:
    def __init__(self,real,imag):
        self.r=real
        self.i=imag
x=coomplex(3.0,-4.5)
x.r,x.i

#example2
class student:
    def __init__(self,n,a):
        self.name=n
        self.age=a
s1=student("anusa",20)
s2=student("haaha",32)
print(s1.age)
print(s2.name)


#finding area of room
class rom:
    length=int(input())
    breath=int(input())
    def clcarea(self):
        area=self.length*self.breath
        print("area is ",area)
a=rom()
a.clcarea()

#finding average of marks using two functions

class student:
    def __init__(self,n,m1=0,m2=0):
        self.name=n
        self.mark1=m1
        self.mark2=m2
    def countavg(self):
        return (self.mark1+self.mark2)/2
    def printavg(self):
        print("average is",self.countavg())
a=student("anusha",20,40)
b=student("banana",40,20)
a.printavg()
b.printavg()


#creating list of objects

class student:
    def __init__(self,n,a):
        self.name=n
        self.age=a
s=[]
n=int(input())
for i in range(0,n):
    na=input()
    a=int(input())
    s.append(student(na,a))
for i in range(0,n):
    print("name "+s[i].name,"age",s[i].age)
#sorting

for i in range(len(s)):
    for j in range(i+1,len(s)):
        if s[i].age>s[j].age:
            s[i],s[j]=s[j],s[i]
for i in range(n):
    print(s[i].name)
    print(s[i].age)

'''
#modules

import file
s=file.add(2,2)
print(s)
















