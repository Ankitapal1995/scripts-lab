from sys import argv
scripts,filename1,filename2=argv
f2=open(filename2,"r")
feat_name=[]
for line in f2:
    line=line.strip("\n")
    feat_name.append(line)
#print(feat_name)
import pandas as pd
data=pd.read_csv(filename1,sep=",",low_memory=False)
data1=data.reindex(columns=feat_name)
#print(data1)
file_name=filename1.rsplit(".",1)[0]
data1.to_csv(file_name+".csv",encoding='utf-8')
