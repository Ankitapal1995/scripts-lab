from sys import argv
scripts,filename=argv
f1=open(filename,"r")
for i in f1:
    i=i.strip('\n')
    i.split("\t")[4]
    print(i)
