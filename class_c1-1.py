#class_c1-1
#22mia1111
import pandas as pd
import numpy as np
data={'maths':[100,85,np.nan,90],'science':[40,55,80,np.nan],'social':[np.nan,70,60,89] }
df=pd.DataFrame(data)
df.isnull()
#df.isnotnull()
'''
#countdf.notnull
#df[maths].notnull
'''
#drop missing values using dropna
df.dropna()
#fillna
df.fillna(40)
#implace-(dataframe will be modified)
#replacemet of values
df['maths'].replace(np.nan,50,inplace=True)
df['science'].replace(np.nan,40,inplace=True)
df['social'].replace(np.nan,30,inplace=True)

#weather problem
import pandas as pd 
import numpy as np
df1=pd.read_csv('/home/ex5/Downloads/weather_na.csv')
df1
df1.isnull().sum()
df1.dropna()
m=round(df1['record_high'].mean(),2)
df1['record_high'].fillna(mean,inplace=True)
minn=df1['avg_low'].min()
maxx=df1['avg_high'].max()
df1['avg_low'].fillna(minn,inplace=True)
df1['avg_high'].fillna(maxx,inplace=True)
df1.describe()
df2=pd.read_csv('/home/ex5/Downloads/weather_na.csv')
df2.describe()
