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

#Q-2 capitalise first word
strr=input()
word=strr.split(" ")
word.upper()
print(word)



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
