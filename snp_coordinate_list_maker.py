from sys import argv
script,filename,queryfile=argv
f=open(filename,"r")
n=f.readlines()
junk=[]
ls_query_cr1=[]
ls_ref_cr=[]
for line in n:
    line= line.strip("\n")
    if line.startswith("#",0):
        junk.append(line)
    else:
        l=line.split("\t")[3]
        c=int(l)
        m=line.split("\t")[4]
        h=int(m)
        n=line.split(';')[5]
        j=n[10::]
        o=j.split("-")
        ls_query_cr1.append(c)
        ls_query_cr1.append(h)
        ls_ref_cr.append(o)
#print(ls_query_cr1)
#print(len(ls_query_cr2))
#print(ls_ref_cr)
ref_cr=[]
for b in ls_ref_cr:
    if len(b)==2:
        if b[0]==b[1]:
            ref_cr.append(int(b[0]))
        else:
            ref_cr.append(int(b[0]))
            ref_cr.append(int(b[1]))
    else:
        ref_cr.append(int(b[0]))
print(ref_cr)
query_cr=[]
for i in ls_query_cr1:
    if i not in query_cr:
        query_cr.append(i)
print(query_cr)

f1=open(queryfile,'r')
query=[]
for i in f1:
    query.append(i)
####
qry=" ".join(query)
#print(qry)

