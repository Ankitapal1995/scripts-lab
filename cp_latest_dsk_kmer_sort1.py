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
#print(ls_line_dsk)
dict1_dsk_data=dict(zip(ls_line_dsk,ls_count_dsk))
#print(dict1_dsk_data)
ls_kmer=[]
ls_count=[]
for line in f2:
    line=line.strip('\n')
    l=line.split()[0]
    n=line.split()[1]
    ls_kmer.append(l)
    ls_count.append(n)
#print(ls_kmer)
#print(ls_count)
#print(ls_mg_count)
dict1=dict(zip(ls_kmer,ls_count))
#dict2=dict(zip(ls_kmer,ls_mg_count))
#print(dict1)
#print(dict2)
f_yes=[]
f_no=[]
for i in ls_line_dsk:
    cnt=0
    for j in ls_kmer:
        if i==j:
            cnt=cnt+1
            f_yes.append(i+"\t"+str(j))
    if cnt==0:
        f_no.append(i+"\t"+"none")
#print(f_yes)
for i in f_no:
    f_yes.append(i)
#print(f_yes)
dsk_kmer_comp={}
for i in f_yes:
    i=i.strip("\n")
    l=i.split()[0]
#    print(l)
    m=i.split('\t')[1]
#    print(m)
    dsk_kmer_comp[l]=m
#print(dsk_kmer_comp)
dsk_ls=[]
sort_ls=[]
for key in dsk_kmer_comp:
    dsk_ls.append(key)
    sort_ls.append(dsk_kmer_comp[key])
#print(dsk_ls)
#print(sort_ls)
for key in ls_kmer:
    if key not in sort_ls:
        sort_ls.append(key)
#print(sort_ls)
dsk_kmer_ct=[]
for i in dsk_ls:
    if i in dict1_dsk_data:
        dsk_kmer_ct.append(dict1_dsk_data[i])
#print(dsk_kmer_ct)
dsk_ct_dt=dict(zip(dsk_ls,dsk_kmer_ct))
#print(dsk_ct_dt)
indi_ct=[]
##mg_ct=[]
for i in sort_ls:
    if i!='none':
        indi_ct.append(dict1[i])
##        mg_ct.append(dict2[i])
    elif i=='none':
        indi_ct.append(0)
##        mg_ct.append(0)
#print(indi_ct)
###print(mg_ct)
frt_ls=[]
##sec_ls=[]
for i in sort_ls:
    frt_ls.append(i)
##    sec_ls.append(i[1])
#print(frt_ls)
###print(sec_ls)
search1=dict(zip(frt_ls,indi_ct))
##search2=dict(zip(sec_ls,mg_ct))
match_ls=[]
for i in dsk_ls:
    if i in search1:
        if dict1_dsk_data[i]==search1[i]:
            match_ls.append("yes")
        else:
            match_ls.append("none")
##    elif i in search2:
##        if dict1_dsk_data[i]==search2[i]:
##            match_ls.append("yes")
##        else:
##            match_ls.append("no")
    else:
        match_ls.append("none")
#print(match_ls)
dif=abs(len(dsk_ls)-len(sort_ls))
if len(sort_ls)>len(dsk_ls):
    dsk_ls.extend(["none"for i in range(dif)])
    dsk_kmer_ct.extend(["none"for i in range(dif)])
    match_ls.extend(["none"for i in range(dif)])
elif len(dsk_ls)>len(sort_ls):
    sort_ls.extend(["none"for i in range(dif)])
    indi_ct.extend(["none"for i in range(dif)])
##    mg_ct.extend(["none"for i in range(dif)])
    match_ls.extend(["none"for i in range(dif)])
else:
    pass
tup=list(zip(dsk_ls,dsk_kmer_ct,sort_ls,indi_ct,match_ls))
#print(tup)
fo=open("final_result_dsk_kmer_sort.csv","w")
#fo.write("dsk")
#fo.write("\t")
#fo.write("dsk_count")
#fo.write("\t")
#fo.write("kmer_count_sort")
#fo.write("\t")
#fo.write("\t")
#fo.write("kmer_count")
#fo.write("\t")
#fo.write("\t")
##fo.write("merge_count")
##fo.write("\t")
#fo.write("count_result")
#fo.write("\n")
for i in tup:
    fo.write(i[0])
    fo.write("\t")
    fo.write(str(i[1]))
    fo.write("\t")
 #   fo.write("\t")
    fo.write(str(i[2]))
    fo.write("\t")
  #  fo.write("\t")
  #  fo.write("\t")
    fo.write(str(i[3]))
    fo.write("\t")
   # fo.write("\t")
   # fo.write("\t")
    fo.write(str(i[4]))
##    fo.write("\t")
##    fo.write("\t")
##    fo.write(str(i[5]))
    fo.write("\n")
fo.close()
