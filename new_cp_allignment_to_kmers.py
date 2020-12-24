from sys import argv
scripts,filename,gff_file=argv
f=open(filename,"r")
readline=f.readlines()
lines_list=[]
bg_algn=[]
ed_algn=[]
junk_ls=[]
seq_ls=[]
for l in readline:
    l=l.strip("\n")
    lines_list.append(l)
#print(lines_list)
    if l.startswith("-- BEGIN",0):
        bg_algn.append(str(l))
        print(bg_algn)
    elif l.startswith('--   END',0):
        ed_algn.append(str(l))
        #print(ed_algn)
    elif l.startswith("/home",):
        junk_ls.append(str(l))
    elif l.startswith("=====",0):
        junk_ls.append(str(l))
    elif l.startswith("-- Alignments",0):
        junk_ls.append(str(l))
    else:
        seq_ls.append(str(l))
#print(seq_ls)
ref_seq_ls1=[]
for k in seq_ls:
    if "^" not  in k:
        ref_seq_ls1.append(k)
########
ref_seq_ls2=list(filter(str.strip,ref_seq_ls1))
#print(ref_seq_ls2)
ref_seq_ls3=[]
for i in ref_seq_ls2:
    #print(i)
    h=i[11:len(i)]
    #print(len(h))
    ref_seq_ls3.append(h)
#print(ref_seq_ls3)
query_ls=[]
sub_ls=[]
for i in ref_seq_ls3[::2]:
    query_ls.append(i)
#print(query_ls)
for j in ref_seq_ls3[1::2]:
    sub_ls.append(j)
#print(sub_ls)
seq_query=[]
seq_sub=[]
for i in query_ls:
    x="".join(query_ls)
seq_query.append(x)
print(seq_query)
for m in sub_ls:
    y="".join(sub_ls)
seq_sub.append(y)
print(seq_sub)
#print(y)
strand=[]
coord1=[]
coord2=[]
for ele in bg_algn:
    f=ele[21::].split(" ")[0]
    j=int(f)
    strand.append(j)
    m=ele[21::].split(" ")[1]
    n=ele[21::].split(" ")[3]
    coord1.append(m)
    coord1.append(n)
    h=ele[21::].split(" ")[5]
    strand.append(h)
    g=ele[21::].split(" ")[6]
    s=ele[21::].split(" ")[8]
    coord2.append(g)
    coord2.append(s)
print(strand)
print(coord1)
print(coord2)
f=open(gff_file,"r")
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

