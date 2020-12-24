from sys import argv
scripts,filename=argv
f1=open(filename,"r")
number=[]
for line in f1:
    line=line.strip("\n")
    l=line.split()[1]
    number.append(l)
#print(number)
ls_prec=[]
for i in number:
    l=int(i)
    if l!=0:
        ls_prec.append("resistant")
    else:
        ls_prec.append("susceptible")
#print(ls_prec)
for i in ls_prec:
    print(i)
