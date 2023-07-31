#notes
#22mia1111
STRING OPERATION
S=''   EMPTY STRING
len(x)   length of string x
S='s\np\ta\x00m'   escape sequences
S="SPAM'S"         double quotes,same as single
S=r'temp\newfolder'   raw string
S[I:J]  i to j numbers will be displayed
"a %s parrot" %kind        string formatting
"a {s} parrot" .format(kind)
S.find('pa')
S.rstrinp()     remove white space to the right
S.replace('pa','xx')    replacement
S.split(',')            split on delimiter
S.isdigit(),isalpha()
A.lower()     case conversion
S.count('abd')  counts the number of letters
S.endswith('?')    checks the last symbol/letter
'spam'.join(strlist)   joins the strings
ord()    will give the haskey value foe given string
chr(89)   will covert hashkey code to character

#excersice 1
s=r'a\n\ob\n\oc'
print(s)
print(len(s))
str="my name is %s" %("anusha")
print(str)
str="i have {0} {1} bird!".format(1,"pretty")
print(str)

#excercise 2
str=input()
print(len(str))
print(str.lower())
print(str.count('a'))
print(ord('A'))
print(chr(98))
for x in str:
    print(x)


#find the sum of haskey code of given name
s=input()
sum=0
for x in s:
    sum+=ord(x)
print(sum)


#indexing

#print first and last character using positive and negetive index
str='name'
n=len(str)
print(str[0])
print(str[n-1])
print(str[-1]) #useful when the length of the string is unknown
print(str[-n])
print(str[2])

#slicing

a[i:j:k]   from i to j-1 elements by k steps only integer inputs are taken


str="string"
print(str[1:4])
print(str[4:1:-1])
print(str[::2])
print(str[::-1])



#check if the given input string is plindrome or not

str=input()
str=str.lower()
if str == str[::-1]:
    print("the given string is palindrome")


#count the number of vowels in your name

str=input()
str=str.lower()
print(str)
vow=str.count('a')+str.count('e')+str.count('i')+str.count('o')+str.count('u')
print(vow)



#check if given pan number is valid or not

str=input()
if len(str)==10:
    if str[0:5].isalpha():
        if str[5:9].isdigit():
            if str[-1].isalpha():
                if str.isupper():
                    print('the given pan is valid')
                else:
                    print('not valid aa')
            else:
                print("not valid a")
        else:
            print("not valid b")
    else:
        print("not valid c")
else:
    print("not valid d")
    
