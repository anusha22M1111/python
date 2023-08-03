
#class 6
#22mia1111

#creating an empty list
L1=[1,2,3,4,5,6]
print(l1[2])
L1[2]=111    access of element using index
delL1[4]    #deleting
len([1,2,3]) #length
[1,2,3]+[4,5,6] #concatanation
[1,2,3,4,5,6]
["Ni!"]*4      #repetition
["Ni!","Ni!","Ni!","Ni!"]
3 in[1,2,3]    #membership
true
for i in range[n] #using indexing
  print[i]
for x in [1,2,3]: #simpler for loop
L=[123,'abc',{}]  #heterogenous
L=[123,'abc',{},[1,2,3,4]]  #sublist
L=list(range(-4,4))

#functions

L.append(4)
L.extend([5,6,7])
L.insert(1,3)   #nserting a a position
L.index(x)
L.count()
L.sort()     #sorted by default
L.reverse()
L.copy()
L.clear()   #removes all elements
L.pop()   #last element will be popped
L.remove(x)
del L[i]  #deleting using index

cmp(L1,L2)  #compare two lists
sum(L1)     #sum of list


#example
L=[]
L=L+[1,2,3]

for i in range(1,3):
    L.append(int(input(i)))
print(L)

res=[]
for c in "spam":
    res+=[c*4]
print(res)

result2=[i for i in range(35,45)]
print(result2)


#read the marks of n student in a class and find the class average

marks=[]
n=int(input())
for i in range(n):
    marks.append(int(input()))
print(marks)
s=sum(marks)/2
print(s)


#find the number of zeros positive numbers and negetive numbers in list

nl=[]
c0=0
c1=0
c2=0
n=int(input())
for i in range(n):
    nl.append(int(input()))
for i in nl:
    if i==0:
        c0+=1
    elif i>0:
        c1+=1
    else:
        c2+=0
print(c0)
print(c1)
print(c2)


#read the names of n students and diaplay the name list in alphabetical order

name=[]
n=int(input())
for i in range(n):
    name.append(input())
name.sort()
print(name)


#watson goces Sherlock a list of N numbers.
#Then he asks him to determine if there exists an element in the list such that the
#sum of the elements on its left is equal to the sum of the elements on its right.
#if there are no elements to the left/right, then the sum is considered to be zero.

num=[]
n=int(input())
for i in range(n):
    num.append(int(input()))
for x in range(0,n):
    if sum(num[0:x])==sum(num[x+1:n]):
        print("element is %d"%num[x])
print("no such element exists")   

    











