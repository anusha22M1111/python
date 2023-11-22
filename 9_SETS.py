#class 9
#22mia1111

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


#intersection
s2=s2 &{1,3}
#difference
s=s-{1,3}
#superset
s>{1,3}


#create two sets s1 and s2 and perform union intersection difference
s1=set()
s2=set()
for i in range(3):
    s=int(input())
    s1.add(s)
for i in range(3):
    s=int(input())
    s2.add(s)
s3=s1|{1,3}
s4=s1&s2
s5=s1-s2
print(s3)
print(s4)
print(s5)


# operations

s.clear()
s.copy() #permanent
s1=s2    #temporary
s=frozenset()  #cannot append or add any elements
s={print(x) for x in range(s)}


#an university has published the results of the term end examination conducted in april.
#list of failures in physics ,maths,chem,and  computer is available .
#write a program to find the number of failures in the examination

phy={"22mia1111","22mia2222","22mia3333"}
chem={"22mia1234","22mia2345","22mia3456","22mia4567"}
math={"22mia5555","22mia6666","22mia4444"}
comp={"22mia1111","22mia1234","22mia4444","22mia2345"}

count=0
for x in phy:
    count+=1
for x in chem:
    count+=1
for x in math:
    count+=1
for x in comp:
    count+=1

print(count)   #14

#alternat
s=set()
s=s|phy|chem|math|(comp)
print(len(s))  #10 (no duplicate elements will be present)



#list=[]
#tuple=()
#set=set()
#dictionary={}

#Dictionary
d={key:value,key2:value2}  #key:value pairs
'''
each pair has key and value
key should be unique
key and value are seperated by:
keys will not be stored in order
'''
unorderd mutable collection

del d['mia']
d.clear()
d[1]='22mia1233'
d.items()
d.keys()
d.viewkeys()
str(d) #for formatting and printing
len(d)


#list vs dictionary
l1=[]
l[99]=spam  #gives error

d{}
d[99]=spam  #works


#example of dictionary

students={'22mia1111':'anusha','22mia2222':'jajaa'}
print(students.values())
print(students.keys())
print(students['22mia1111'])
print(students)


#getting input and creating a dictionary

d={}
n=int(input())
for i in range(n):
    k=input("regno")
    v=input("name")
    d[k]=v
print(d)

#nesting in dictionary
rec={'name':'bob',
     'jobs':['developer','manager']}

#record sum
#rec={rollno:[name,cat1,cat2,fat]}

f={1111:['anusa',12,13,45],
   1234:['annkk',34,56,25]}
print(str(f))

d={}
n=int(input())
for i in range(0,n):
    k=input()
    l=[]
    for i in range(4):
        l.append(input())
    d[k]=l

print(d)
