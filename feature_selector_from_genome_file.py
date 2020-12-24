from sys import argv
scripts,filename1,filename2=argv
f1=open(filename1,"r")
f2=open(filename2,"r")
ls_kmr=[]
#ls_count=[]
for l in f1:
    l=l.strip("\n")
    m=l.split()[0]
#    n=l.split()[1]
    ls_kmr.append(m)
ls_features=[]
for k in f2:
    k=k.strip("\n")
    h=k.split()[0]
    ls_features.append(h)
a=set(ls_kmr)
b=set(ls_features)
c=(a & b)
print(len(c))
#dif_a = a - b
dif_b = b - a
print(len(dif_b))
dict1={}
dict2={}
for i in c:
    dict1[i]=int(1)
#print(dict1)
for j in dif_b:
    dict2[j]=int(0)
#print(dict2)
dict1.update(dict2)
print(len(dict1))
#filename="1773.5838.h5_countbinary.txt"
filewrite=filename1[0:-15]+"kmer_matrix.csv"
#print(filewrite)
fo = open(filewrite,"w")
for i in dict1:
    fo.write(i)
    fo.write(" ")
    fo.write(str(dict1[i]))
    fo.write("\n")
fo.close()

