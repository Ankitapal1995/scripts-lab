from sys import argv
scripts,filename1,filename2,filename3=argv
f1=open(filename1,"r")
f2=open(filename2,"r")
f3=open(filename3,"r")
ls_f1=[]
ls_f2=[]
ls_f3=[]
for line in f1:
    line=line.strip("\n")
    l=line.split("\t")[0]
    ls_f1.append(l)
#print(ls_f1)
#print(len(ls_f1))
for line in f2:
    line=line.strip("\n")
    m=line.split("\t")[0]
    ls_f2.append(m)
#print(ls_f2)
#print(len(ls_f2))
for line in f3:
    line=line.strip("\n")
    p=line.split("\t")[0]
    ls_f3.append(p)
#print(len(ls_f3))

merge_list=[]
for i in ls_f1:
    merge_list.append(i)
for j in ls_f2:
    merge_list.append(j)
for k in ls_f3:
    merge_list.append(k)
#print(merge_list)
#print(len(merge_list))
for r in merge_list:
    print(r)
