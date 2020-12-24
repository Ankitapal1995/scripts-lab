from sys import argv
scripts,filename=argv
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
for i in query_ls:
    x="".join(query_ls)
print(x)
for m in sub_ls:
    y="".join(sub_ls)
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
final_query=[]
print(x)
print(y)
if int(coord1[0]) < int(coord1[1]):
    k=int(coord1[0])
    g=('N'*k)+x
    final_query.append(g)
elif int(coord1[0]) > int(coord1[1]):
    k=int(coord1[1])
    g=('N'*k)+x[::-1]
    final_query.append(g)
else:
    a=2
print(len(final_query))
final_sub=[]
if int(coord2[0])< int(coord2[1]):
    k=int(coord2[0])
    g=('N'*k)+y
    final_sub.append(g)
elif int(coord2[0]) > int(coord2[1]):
    k=int(coord2[1])
    g=('N'*k)+y[::-1]
    final_sub.append(g)
print(len(final_sub))
f1=open(filename+"_query.csv","w")
for i in final_query:
    f1.write(i)
f1.close()

f2=open(filename+"_sub.csv","w")
for i in final_sub:
    f2.write(i)
    f2.close()
