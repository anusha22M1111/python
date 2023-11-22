#class 8
#22mia1111

#Tuples
l1=[1,2,3]   #lists are mutable 
t=(10,20,30) #but tuples are immutable
t=(50,)      #one element should be followed by a comma
l1=list(t)   #typecasting tuple to list
t1=tuple(l1) #typecating list to tuple
sorted(t)    #will sort the tuple and return a list
#concatenantion
#repetition
t.index(2)   #indexing
t.count(3)   #counting number of elements

t=(20,20.3,"aa",["aaa","ss"])
t[3][1]      #returns ss




#basic tuple input reading

n=int(input())
a=()
t2=()
for i in range(n):
    a=a+(int(input()),)
print(a)
for x in a:
    t2=t2+(x*x,)
print(t2)
print(sorted(t2))


#hospital problem (the test results must not be altered)
#we use tuple for sensitive content like this

a=()
for i in range(5):
    a=a+(float(input()),)

if a[0]<20 or a[0]>30:
    print("not normal")
else:
    print("normal")
    
if a[1]<35.5 or a[1]>40:
    print("not normal")
else:
    print("normal")
    
if a[2]<12 or a[2]>15:
    print("not normal")
else:
    print("normal")
    
if a[3]<120 or a[3]>150:
    print("not normal")
else:
    print("normal")
    
if a[4]<80 or a[4]>120:
    print("not normal")
else:
    print("normal")
    
 
#solution

a=()
minv=(20,35.5,12,120,80)
maxv=(30,40,15,150,120)
for i in range(5):
    a=a+(input(),)
for i in range(0,5):
    if(a[i]=="N"):
        print("test not taken")
        continue
    if(float(a[i])>minv[i] and float(a[i])<maxv[i]):
        print("normal")
    else:
        print("abnormal")
        


#sets

#an unordered collection of unique and immutable object that supports operations
#operations
union         |
intersection  &
difference    -
s={1,2,3,4,5}
s=set()   #empty set
d={}      #dictionary
s.add()   #adding element in set

#reading values for set
n=int(input())
s=set()
for i in range(n):
    val=int(input())
    #s.add(val)
    s=s|{val}
print(s)
print(len(s))

#indexing and slicing is not permitted in set

