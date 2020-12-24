from sys import argv
script,filename=argv
f=open(filename,"r")
ls_kmer=[]
ls_ct=[]
for line in f:
    line=line.strip("\n")
    l=line.split()[0]
    m=line.split()[1]
    ls_kmer.append(l)
    ls_ct.append(m)
#print(ls_kmer)
#print(ls_ct)
ls_ct_new=[]
for i in ls_ct:
    j=int(i)
    if j!=0:
        ls_ct_new.append(int(1))
    else:
        pass
print(ls_ct_new)
print(len(ls_ct_new))


#ct_ls=[]
#cnt=0
#for i in ls_ct:
#    cnt=cnt+int(i)
#    ct_ls.append(cnt)
##print(ct_ls)
#total=ct_ls[(len(ct_ls)-1)]
##print(total)
#frq_ls=[]
#for ct in ls_ct:
#    frq=int(ct)/int(total)
#    fre=round(frq,6)
#    frq_ls.append(fre)
##print(frq_ls)
dict1=dict(zip(ls_kmer,ls_ct_new))
##print(tup)
file_name=filename.rsplit(".",1)[0]
fo=open(file_name+"_countbinary.txt","w")
for i in dict1:
    fo.write(i)
    fo.write(" ")
    fo.write(str(dict1[i]))
    fo.write("\n")
fo.close()
