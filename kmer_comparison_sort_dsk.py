from sys import argv
script,filename1,filename2=argv
f1=open(filename1,"r")
f2=open(filename2,'r')
ls_line_dsk=[]
ls_count_dsk=[]
for line in f1:
    line=line.strip("\n")
    l=line.split()[0]
    m=line.split()[1]
    ls_line_dsk.append(l)
    ls_count_dsk.append(m)
##print(ls_line_dsk)
dict1_dsk_data=dict(zip(ls_line_dsk,ls_count_dsk))
#print(f"dsk data {dict1_dsk_data}")
ls_kmer=[]
ls_count=[]
for line in f2:
    line=line.strip('\n')
    l=line.split("  ")[0]
    n=line.split("  ")[1]
    ls_kmer.append(l)
    ls_count.append(n)
##print(ls_kmer)
##print(ls_count)
##print(ls_mg_count)
dict1=dict(zip(ls_kmer,ls_count))
#dict2=dict(zip(ls_kmer,ls_mg_count))
#print(f"kmer sort data {dict1}")
def rev_comp(s):
    base_complement={'A':'T','C':'G','G':'C','T':'A','n':'n','o':'o'}
    letters=list(s)
    letters=[base_complement[base]for base in letters]
    return''.join(letters)[::-1]
##print(dict2)
f_yes=[]
f_no=[]
for i in ls_kmer:
    cnt=0
    for j in ls_line_dsk:
        if i==j:
            cnt=cnt+1
            x=(i,j)
            f_yes.append(x)
        elif i==rev_comp(j):
            cnt=+1
            x=(i,j)
            f_yes.append(x)
    if cnt==0:
        x=(i,"no")
        f_yes.append(x)
#print(f_yes)
for i in ls_line_dsk:
    cnt=0
    for j in ls_kmer:
        if i==j:
            cnt=+1
        elif i==rev_comp(j):
            cnt=+1
    if cnt==0:
        x=("no",i)
        f_yes.append(x)
#print(f_yes)
dsk_mt_ct=[]
kmer_mt_ct=[]
for k in f_yes:
    if k[0]!="no" and k[1]!="no":
        kmer_mt_ct.append(dict1[k[0]])
        dsk_mt_ct.append(dict1_dsk_data[k[1]])
    elif k[0]=="no":
        kmer_mt_ct.append("none")
        dsk_mt_ct.append(dict1_dsk_data[k[1]])
    elif k[1]=="no":
        kmer_mt_ct.append(dict1[k[0]])
        dsk_mt_ct.append("none")
    else:
        pass
##print(dsk_mt_ct)
##print(kmer_mt_ct)
ct_table=list(zip(kmer_mt_ct,dsk_mt_ct))
kmer_info=[]
for i in f_yes:
    if i[0]==i[1]:
        kmer_info.append("exact match")
    elif i[0]==rev_comp(i[1]):
        kmer_info.append("reverse comp")
    else:
        kmer_info.append("not matched")
##print(kmer_info)
ct_info=[]
for h in ct_table:
    if h[0]==h[1]:
        ct_info.append("matched")
    else:
        ct_info.append("not matched")
##print(ct_info)

final_tup=list(zip(f_yes,ct_table,kmer_info,ct_info))

fo =open(filename1.partition(".")[0]+"_kmer_sort_dsk_comp.csv","w")
fo.write("kmer sort ")
fo.write("\t")
fo.write("dsk ")
fo.write("\t")
fo.write("kmer sort count")
fo.write("\t")
fo.write("dsk count")
fo.write("\t")
fo.write("kmer comp")
fo.write("\t")
fo.write("count comp")
fo.write("\n")
for i in final_tup:
    fo.write(i[0][0])
    fo.write("\t")
    fo.write(i[0][1])
    fo.write("\t")
    fo.write(str(i[1][0]))
    fo.write("\t")
    fo.write(str(i[1][1]))
    fo.write("\t")
    fo.write(i[2])
    fo.write("\t")
    fo.write(i[3])
    fo.write("\t")
    fo.write("\n")
fo.close()






