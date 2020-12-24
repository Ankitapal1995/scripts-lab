from sys import argv
scripts,filename1,filename2=argv
f1=open(filename1,"r")
ls_kmers_res=[]
for line in f1:
    line=line.strip("\n")   
    l=line.split()    
    g=" ".join(map(str,l))
    ls_kmers_res.append(g)
#print(len(ls_kmers_res))
f2=open(filename2,"r")
ls_kmers_sus=[]
for line in f2:
    line=line.strip("\n")
    k=line.split()
    h=" ".join(map(str,k))
    ls_kmers_sus.append(h)
#print(len(ls_kmers_sus))
a=set(ls_kmers_res)
b=set(ls_kmers_sus)
c=(a & b)
#print(c)
for i in c:
    print(i)
