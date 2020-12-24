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
        #print(bg_algn)
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
#for i in seq_ls:
#    print(i[1])
#print(ref_seq_ls1)

########
#seq_ls1=list(filter(str.strip("\n"),seq_ls))
#print(seq_ls1)
ref_seq_ls=[]
for i in seq_ls:
    #print(i)
    h=i[11:len(i)]
    #print(h)
    ref_seq_ls.append(h)
#print(ref_seq_ls)
while '' in ref_seq_ls:
    ref_seq_ls.remove('')
#print(ref_seq_ls)
query_ls=[]
sub_ls=[]
snp_coord=[]
for i in ref_seq_ls[::3]:
    query_ls.append(i)
#print(query_ls)
for j in ref_seq_ls[1::3]:
    #print(len(j))
    sub_ls.append(j)
#print(sub_ls)
for i in ref_seq_ls[2::3]:
    #print(len(i))
    snp_coord.append(i)
#print(snp_coord)
query_s="".join(query_ls)
sub_s="".join(sub_ls)
query_seq=query_s.replace(".","n")
sub_seq=sub_s.replace(".","n")
            
snp_count="".join(snp_coord)
#print(len(query_seq))
#print(len(sub_seq))
#print(snp_count)
strand=[]
coord1=[]
coord2=[]
for ele in bg_algn:
    f=ele[21::].split(" ")[0]
    j=int(f)
    strand.append(j)
    m=ele[21::].split(" ")[1]
    n=ele[21::].split(" ")[3]
    coord1.append(int(m))
    coord1.append(int(n))
    h=ele[21::].split(" ")[5]
    strand.append(int(h))
    g=ele[21::].split(" ")[6]
    s=ele[21::].split(" ")[8]
    coord2.append(int(g))
    coord2.append(int(s))
#print(strand)
#print(coord1)
#print(coord2)
snp_ls=[x for x,v in enumerate(snp_count) if v=="^"]
query_31mers_ls=[]
sub_31mers_ls=[]
for i in snp_ls:
#    print(query_seq[i])
    query_31mers_ls.append(query_seq[(i-30):(i+1)])
    sub_31mers_ls.append(sub_seq[(i-30):(i+1)])
#print(query_31mers_ls)
#print(sub_31mers_ls)
    #print(sub_seq[i])
#def reverse_comp(string):
#    ls=[]
#    dict1={"a":"t","t":"a","g":"c","c":"g"}
#    for i in string[::-1]:
#        i=dict1[i]
#        ls.append(i)
#    x=''.join(ls)
#    return(x)
#final_query_31mer=[]
#final_sub_31mer=[]
#for i in query_31_mers_ls:
#    if strand[0]==-1:
#        j=reverse_comp(i)
#        final_query_31mer.append(j)
#    else:
#        final_query_31mer.append(i)
##print(final_query_31mer)
########
#for i in sub_31_mers_ls:
#    if strand[1]==-1:
#        j=reverse_comp(i)
#        final_sub_31mer.append(j)
#    else:
#        final_sub_31mer.append(i)
#print(final_sub_31mer)

f1=open(filename[:-3]+"_query.csv","w")
for i in query_31mers_ls:
    f1.write(i.upper())
    f1.write("\n")
f1.close()
f2=open(filename[:-3]+"_sub.csv","w")
for i in sub_31mers_ls:
    f2.write(i.upper())
    f2.write("\n")
f2.close()

