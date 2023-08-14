#practise test 1
#22mia1111

#question 1
L=["milk bikis","tiger","marie","dream cream","choco cream"]
L1=[["milk bikis","tiger","marie","dream cream","choco cream"],[10,5,12,7,5],[10,5,10,15,15]]
n=int(input())
tot=0
for i in range (n):
    order=input("biscuit name:")
    quan=int(input("quantity:"))

    j=L.index(order)
    if L1[1][j]<quan:
        continue
    else:
        for i in range(quan):
            tot+=L1[2][j]
            L1[1][j]-=1
print(tot)

#question 2

import re
str=input()
if len(str)>12 or len(str)<6:
    print("invvalid")
else:
    if re.match("^((?=.*?[a-z])(?=.*?[0-9])(?=.*?[A-Z])(?=.*?[$#@]).{6})$",str):
        print("valid")
    else:
        print("invalid")


