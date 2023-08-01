
#class 5
#22mia1111

#develop a security system that works with the caeser cipher
#the given word will be converted to 3keys away from the current charachter

print(ord('a'))
str=input()
key=int(input())
str=str.lower()
cc=""
for x in str:
    hkey=ord(x)
    new=hkey+key
    if new>122:
        new=new-26
    cc=cc+chr(new)
print(cc)


#regular expression
symbol     description
literal    match literal string value
re1|re2    matching re1 and re2
.          any charachter
^          start
$          end
*          match 0 or more of pattern
+          match 1 or many 
?          match 0 or 1
{N}        N occurence is mandatory
{N,M}      N to M occurance
[]         match any single charechter from given ch
[ - ]      match any single charechter in range of ch
[^ ]       shoudnt match this pattern

syntax
re.match(pattern,string)


import re
str=input()
if re.match("f.o$",str):
    print("matched")
else:
    print("unmatched")


# check weather the given registration numbr is valid or not

import re
str="22MIA1111"
if re.match("^[1-9][0-9][A-Z]{3}[0-9]{4}$",str):
    print("valid")
else:
    print("invalid")



#check for mobile number

import re
str="9838384885"
if re.match("^[1-9][0-9]{9}$",str):
    print("valid")
else:
    print("invalid")


#check valid pan number

import re
str="ABCDS1234Z"
print("valid") if re.match("^[A-Z]{5}[0-9]{4}[A-Z]$",str) else print("invalid")
  
#CHECK FOR floating point number
import re
str="-05.5"
print("valid") if re.match("^\-?[1-9][0-9]\.?[0-9]*$",str) else print("invalid")


