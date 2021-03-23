from sys import argv
script,filename=argv
f=open(filename,"r")
ls_kmer=[]
ls_count=[]
for line in f:
        line=line.strip()
        l=line.split()[0]
        m=line.split()[1]
        ls_count.append(l)
        ls_kmer.append(m)
dict1=dict(zip(ls_kmer,ls_count))
def rev_comp(s):
    base_complement={'A':'T','C':'G','G':'C','T':'A'}
    letters=list(s)
    letters=[base_complement[base]for base in letters]
    return''.join(letters)[::-1]

merge_dic={}
for key in dict1:
    re=rev_comp(key)
    o_kmer_count=int(dict1[key])
    if re in dict1:
        if re!=key:
           r_kmer_count=int(dict1[re])
           t_count=o_kmer_count+r_kmer_count
           merge_dic[(key,re)]=t_count
        elif re==key:
            t_count=o_kmer_count
            merge_dic[(key,key)]=t_count
    else:
        t_count=o_kmer_count
        merge_dic[(key,key)]=t_count
#print(merge_dic)
final_ls=[]
for key in merge_dic:
    x=list(key)
    y=sorted(x)
    final_ls.append(y)
#print(final_ls)
import itertools
final_ls.sort()
new_final_ls=list(final_ls for final_ls,_ in itertools.groupby(final_ls))
#print(new_final_ls)
tup=[tuple(l) for l in new_final_ls]
#print(tup)
final_dic={}
for key in tup:
    final_dic[key]=merge_dic[key]
#print(final_dic)
for key in final_dic:
    print(key,"\t",final_dic[key])



