from sys import argv
scripts,filename=argv
f=open(filename,"r")
ls_true=[]
ls_false=[]
for line in f:
    line=line.strip("\n")
    l=line.split()[1]
    k=int(l)
    if k==0:
        ls_true.append(k)
    else:
        ls_false.append(k)
print(ls_true)
print(ls_false)
print(len(ls_true))
print(len(ls_false))
