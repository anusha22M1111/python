#class_11
#22mia1111
'''
#sorting algorithm
def swap(a,b):
    temp=a
    a=b
    b=temp
    return(a,b)
l=[3,4,5,1,2]
for i in range(5):
    for j in range(5):
        if l[i]<l[j]:
            l[i],l[j]=swap(l[i],l[j])
print(l)

#sorting method 2
l=[3,4,5,1,2]
n= len(l)
for i in range(n):
    for j in range(n-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print(l)

#file handling

#opening a file
file object=open(file name,[access mode],[buffering])
r  = read only
w  = write only
a  = append only
r+ = read and write
w+ = write and read
a+ = append and read

#attributes
file.closed  --#checks weather file is closed
file.mode    --#returns the mode of the file eg:w+
file.name    --#returns name of the file

#procedure to open a file

f1 =open("/home/ex5/mia.txt","r")
print("name of the file:",f1.name)
print("mode of the file:",f1.mode)
print("closed or not : ",f1.closed)

#functions for file handling
read()         --return 1 string
readline()     --returns one line
readlines()    --returns list of lines

write()        --writes fixed characters
writeline()    --write a list of string
writelines()

#example-read

f1 =open("/home/ex5/mia.txt","r")
fcontent=f1.read()
print(len(fcontent))
f1.seek(0)        #---to start reading from the first string
fline=f1.readlines()
print(len(fline))

#example-write

f1 =open("/home/ex5/mia.txt","w")
f1.write("shasha jijji")
f1.close()

#copy contents from sample one to sample two

f1 =open("/home/ex5/sample1.txt","r")
fline=f1.readlines()
print(fline)

f2 =open("/home/ex5/sample2.txt","w")
f2.writelines(fline)
f2.close()
f1.close()


#find no of charachters,line,words in a file 


f1 =open("/home/ex5/sample1.txt","r")
fcontent=f1.read()
print(len(fcontent))
f1.seek(0)
fline=f1.readlines()
print(len(fline))
fwords=fcontent.split(" ")
print(len(fwords))


#alternate for this
def charcount(f1):
    return len(open(f1).read())
def wordcount(f1):
    return len(open(f1).read().split(" "))
def linecount(f1):
    return len(open(f1).readlines())
fconten=charcount("/home/ex5/sample1.txt")
print(fconten)
fw=wordcount("/home/ex5/sample1.txt")
fl=linecount("/home/ex5/sample1.txt")
print(fw)
print(fl)
'''
#copy marks in csv file and copy the contents with tolal marks

f1=("/home/ex5/Documents/pymark.csv")



















