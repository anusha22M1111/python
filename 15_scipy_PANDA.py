#class_15
#22mia1111
#linear algebra using numpy

import numpy as np

a=np.array([[4,3],[-5,9]])
b=np.array([[20],[26]])
#X=np.linalg.inv(a).dot(b)
X=np.linalg.solve(a,b)
print(X)
aa=np.array([[6,1,1],[4,-2,5],[2,8,7]])
print(np.linalg.matrix_rank(aa))

#o/p
[[2.]
 [4.]]
3

##notes
matrix_rank  ----rank of the matrix is given
dot         ----givs dot product of two matrix
trace         ---trace of the matrix
inv         ----gives inverse of matrix
matrix_power  ---gives power of matix
eigh          ---eigen values and vectors
eigvals      ----only eigen values
ravel         ---

a=np.array([[1,2j],[2j,5]])
print(a)
c,d=np.linalg.eigh(a)
print(c)
print(d)

#o/p
[[1.+0.j 0.+2.j]
 [0.+2.j 5.+0.j]]
[0.17157288 5.82842712]
[[-0.92387953+0.j         -0.38268343+0.j        ]
 [ 0.        +0.38268343j  0.        -0.92387953j]]
 
aa=np.array([[6,1,1],[4,-2,5],[2,8,7]])
b=np.ravel(aa,order='C')
print(b)
print(np.ravel(aa,order='F'))

#o/p
[ 6  1  1  4 -2  5  2  8  7]
[ 6  4  2  1 -2  8  1  5  7]

#SCIPY
import scipy
a=np.array([[7,2],[4,5]])
b=np.array([8,10])
res=scipy.linalg.solve(a,b)
print(res)

#practice question
#q-1
q1=np.array([[4,3,2],[-2,2,3],[3,-5,2]])
q11=np.array([[25],[-10],[-4]])
print(np.linalg.solve(q1,q11))

#o/p
[[ 5.]
 [ 3.]
 [-2.]]
#q-2
#create a function to calculate the rank ,determinant and
#inverse of a square matrix using Numpy
def fun(a):
    print(np.linalg.matrix_rank(a))
    print(np.linalg.det(a))
    print(np.linalg.inv(a))

q2=np.array([[7,2],[4,5]])
fun(q2)

#output
2
27.0
[[ 0.18518519 -0.07407407]
 [-0.14814815  0.25925926]]
#panda
#python and data analysis /panal data system
#has three data structures
-series   -1D
-dataframe -2D
-panel     -3D

#panda series
pandas.Series(data,index,datatype,copy)
index need not be integer
datatype is optional itll infer by itself if not mentionsed
copy copies the change in series to orginal array if true
copy is false by default

import pandas as pd

#using array
data=np.array([1,2,3,4,55])
print(pd.Series(data))

#using list
i=['a','s','d']
print(pd.Series(i))
sub=['maths','english','science']
mark=[11,22,33]
print(pd.Series(mark,index=sub))

#using dictionary
subb={'math':100,'science':98,'english':100}
print(pd.Series(subb))

#series with missing values
subj=['math','science','english','computerscience']
b=pd.Series(subb,index=subj)
print(b)

#extracting values
print(b[b>99])
#to sort
c=b.sort_values()
print(c)
#creating rank
d=b.rank()
print(d)


#output
0     1
1     2
2     3
3     4
4    55
dtype: int64
0    a
1    s
2    d
dtype: object
maths      11
english    22
science    33
dtype: int64
math       100
science     98
english    100
dtype: int64
math               100.0
science             98.0
english            100.0
computerscience      NaN
dtype: float64
math       100.0
english    100.0
dtype: float64
science             98.0
math               100.0
english            100.0
computerscience      NaN
dtype: float64
math               2.5
science            1.0
english            2.5
computerscience    NaN
dtype: float64

#inbuilt functions in series
print(b.sum())
print(b.mean())
print(b.median())
print(b.std())
print(b.max())
print(b.idxmax())
print(b.min())
print(b.idxmin())
print(b.count())

#o/p
298.0
99.33333333333333
100.0
1.1547005383792517
100.0
math
98.0
science
3
