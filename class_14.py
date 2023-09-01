#class 14
#22mia1111

#binary operators

a-b
a+b
np.subtract()
np.add()
np.dot()
np.multiply()
newarr=np.array([1,2,3,4,5])

#universal functions

mod() or reminder() returns the reminder
divmod() returns quotient as well as reminder 2outputs
absolute() returns positve values of elements
trunc() or fix() will reduce the decimal points
around() round it to two decimal places
floor() nearest lower integer
cell()
gcd() returns the gcd for integers
lcm()
gcd.reduce() returns the gcd for array
log() log2() log10()

import numpy as np
a=np.array([1,2,3,4])
b=np.array([2,3,4,5])
c=np.add(a,b)
d=np.subtract(b,a)
e=np.multiply(a,b)
f=np.mod(a,b)
g=np.divmod(a,b)

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)

#output
[1 2 3 4]
[2 3 4 5]
[3 5 7 9]
[1 1 1 1]
[ 2  6 12 20]
[1 2 3 4]
(array([0, 0, 0, 0]), array([1, 2, 3, 4]))

#linear algebra with numpy


#trace -sum of diagonals
#rank-number of pivots
#eigen values and vectors


import numpy as np
a=np.array([[1,2],[1,2]])
b=np.array([[2,3],[2,3]])
e=a.dot(b)
c=np.dot(a,b)
d=np.vdot(a,b)
print(a)
print(b)
print(c)
print(d)
print(e)

#outputs- [[1 2]
 [1 2]]
[[2 3]
 [2 3]]
[[6 9]
 [6 9]]
16
[[6 9]
 [6 9]]
 

import numpy as np

data=[[4,3],[-5,9]]
a=np.array(data)
b=np.array([[20],[26]])
c=np.linalg.inv(a).dot(b)    #[[2.],[4.]]
print(c)
d=np.linalg.solve(a,b)        #[[2.],[4.]]
print(d)

e=np.linalg.matrix_rank(a)
f=np.linalg.det()
g=np.trace()
