from sys import argv
scripts,filename,u,j=argv
f=open(filename,"r")
h=int(u)
s=int(j)
ls_ct=[]
ls_kmer=[]
for line in f:
    line=line.strip("\n")
    l=line.split()[0]
    l1=int(l)
    m=line.split()[1]
    ls_ct.append(l1)
    ls_kmer.append(m)
dict1=dict(zip(ls_kmer,ls_ct))
#for key in list(dict1):
#    if dict1[key]==1 or dict1[key]==2:
#        del dict1[key]
#print(dict1)
dict2={k:v for k,v in dict1.items() if v!=h and v!=s}
file_name=filename+".csv"
f1=open(file_name,"w")
for i in dict2:
   f1.write(str(dict2[i]))
   f1.write(" ")
   f1.write(i)
   f1.write("\n")
f1.close()
