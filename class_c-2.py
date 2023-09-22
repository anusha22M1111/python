#class_c-2
#22mia1111
import pandas as pd
import numpy as np
from datetime import datetime
#used to extrate the date and time as it is
#converts the string to datetime
pd.date_range(start='2/2/2019',end='2/08/2019')

   op:DatetimeIndex(['2019-02-02', '2019-02-03', '2019-02-04', '2019-02-05',
               '2019-02-06', '2019-02-07', '2019-02-08'],
              dtype='datetime64[ns]', freq='D')

   
#create a date range with timestamps of hourly frequency
date_r=pd.date_range(start='2/2/2019',end='2/08/2019',freq=H)
date_r


  op:DatetimeIndex(['2019-02-02 00:00:00', '2019-02-02 01:00:00',
               '2019-02-02 02:00:00', '2019-02-02 03:00:00',
               '2019-02-02 04:00:00', '2019-02-02 05:00:00',
               '2019-02-02 06:00:00', '2019-02-02 07:00:00',
               '2019-02-02 08:00:00', '2019-02-02 09:00:00',
               ...
               '2019-02-07 15:00:00', '2019-02-07 16:00:00',
               '2019-02-07 17:00:00', '2019-02-07 18:00:00',
               '2019-02-07 19:00:00', '2019-02-07 20:00:00',
               '2019-02-07 21:00:00', '2019-02-07 22:00:00',
               '2019-02-07 23:00:00', '2019-02-08 00:00:00'],
              dtype='datetime64[ns]', length=145, freq='H')

#finding days in intervals
pd.date_range(start='2/2/2019',periods=8)

  op:DatetimeIndex(['2019-02-02', '2019-02-03', '2019-02-04', '2019-02-05',
               '2019-02-06', '2019-02-07', '2019-02-08', '2019-02-09'],
              dtype='datetime64[ns]', freq='D')


#converting string to datetime in dataframe
d={'date':['3/10/2020','3/10/2020','3/12/2000'],'values':[2,3,4]}
df=pd.DataFrame(d)
df['date']=pd.to_datetime(df['date'])
print(df)


ip:
 date  values
0  3/10/2020       2
1  3/10/2020       3
2  3/12/2000       4
op:
date  values
0 2020-03-10       2
1 2020-03-10       3
2 2000-03-12       4

#errors='ignore' 
#errors='coerce' op- error data will be stored as naT
df1=pd.DataFrame({'name':['anusha','aaaa','sdddd','esds','fdsdf','sdfsdf','sdfsdf','qwwer'],'dob':['3/4/2000','3/4/2000','4/3/2000','4/3/2000','4/3/2000','4/3/2000','4/3/2000','4/3/2000']})
print(df1)


   op:  name       dob
0  anusha  3/4/2000
1    aaaa  3/4/2000
2   sdddd  4/3/2000
3    esds  4/3/2000
4   fdsdf  4/3/2000
5  sdfsdf  4/3/2000
6  sdfsdf  4/3/2000
7   qwwer  4/3/2000

df1['dob']=pd.to_datetime(df1['dob'])
print(df1)


op:
    name        dob
0  anusha 2000-03-04
1    aaaa 2000-03-04
2   sdddd 2000-04-03
3    esds 2000-04-03
4   fdsdf 2000-04-03
5  sdfsdf 2000-04-03
6  sdfsdf 2000-04-03
7   qwwer 2000-04-03

today=pd.to_datetime('today')
df1['age']=today.year-df1['dob'].dt.year
df1


   op:
       name	dob	age
0	anusha	2000-03-04	23
1	aaaa	2000-03-04	23
2	sdddd	2000-04-03	23
3	esds	2000-04-03	23
4	fdsdf	2000-04-03	23
5	sdfsdf	2000-04-03	23
6	sdfsdf	2000-04-03	23
7	qwwer	2000-04-03	23

df1['year']=df1['dob'].dt.year
df1['month']=df1['dob'].dt.month
df1['day']=df1['dob'].dt.day
df1


op:
    name	dob	age	year	month	day
0	anusha	2000-03-04	23	2000	3	4
1	aaaa	2000-03-04	23	2000	3	4
2	sdddd	2000-04-03	23	2000	4	3
3	esds	2000-04-03	23	2000	4	3
4	fdsdf	2000-04-03	23	2000	4	3
5	sdfsdf	2000-04-03	23	2000	4	3
6	sdfsdf	2000-04-03	23	2000	4	3
7	qwwer	2000-04-03	23	2000	4	3


#select data with a specific year and perform aggregation
df1=df1.set_index(['dob'])
df1

df1.loc['2000','age'].sum()
op:184


df1['2000'].groupby('month').sum()


op:	age	year	day
month			
3	46	4000	8
4	138	12000	18

#groupby by particular month
cond=df1.index.month==3
df1[cond]

op:name	age	year	month	day
dob					
2000-03-04	anusha	23	2000	3	4
2000-03-04	aaaa	23	2000	3	4

#JOSN
#here the dictionary is stored as string
#loads=readins from a string
#load =read from file
'''
p='{'name':'ram','contact':[12343534,123424523]}'
f=open("content/friuts.jason",'r+')
data=json.load(f)
df=pd.dataframe(data)df1=pd.read_json('/contetn/frit.json')
str=#dictionary
str=json.dumps('')
json.dump()
df.to_json('/content/')

'''

import json
dff=pd.read_json('/home/ex5/Downloads/sampledata.json')
dff
