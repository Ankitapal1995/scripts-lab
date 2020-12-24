from sys import argv
scripts,filename=argv
f=open(filename,'r')
import pandas as pd
import numpy as np
dataset=pd.read_csv(filename,sep=",",low_memory=False , header= None)
#print(dataset)
df=dataset.iloc[1:]
df=df.apply(pd.to_numeric)
#print(df)
#df1=df.where(df== 0, 1)
#print(df1)
#da=pd.DataFrame(np.where(df > 0, 1, 0),index =df.index ,colummns= df.columns)
#dataset.replace(to_replace = 0 , value = "NaN")
#print(dataset)
#print(da)
#dataset.columns[dataset.isnull().sum() <6]
#print(dataset.isnull().mean())
#print(dd)
#dataset.columns[dataset.isnull().mean() <6]
#di=dataset[dataset.columns[dataset.isnull().mean() < 0.6923]]
#print(di)
#num = df._get_numeric_data()
#num1=num._get_numeric_data()
#num[num==0]="NaN"
#num[num >0 ] =1
#print(df)
#df.to_csv("updated"+filename+".csv")
df1=df.astype(bool).sum(axis=0)
df2=df.astype(bool).sum(axis=1)
print(df1)
df3=df.loc[(df2 !=0),(df1 !=7)]
print(df3)
