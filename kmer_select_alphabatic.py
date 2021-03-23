from sys import argv
script,filename=argv
fo=open(filename,"r")
ls_kmer1=[]
ls_kmer2=[]
ls_count=[]
for line in fo:
    line=line.strip("\n")
    l=line.split("\t")[0]
    h=l.replace("(","") 
    g=h.replace(")","")
    n=g.replace("'","")
    j=n.split(",")[0]
    c=(n.split(",")[1]).strip()
    ls_kmer1.append(j)
    ls_kmer2.append(c)
    n=line.split("\t")[1]
    #print(d)
    ls_count.append(n)
f_ls=list(zip(ls_kmer1,ls_kmer2))
#print(f_ls)
def rev_comp(s):
    base_complement={'A':'T','C':'G','G':'C','T':'A'}
    letters=list(s)
    letters=[base_complement[base]for base in letters]
    return''.join(letters)[::-1]
ls_kmer=[]
for i in ls_kmer1:
    re=rev_comp(i)
    k=(i,re)
    ls_kmer.append(k)
#print(ls_kmer)
f_ls_kmer=[]
for i in ls_kmer:
    j=list(i)
    l=sorted(j)
    f_ls_kmer.append(l[0])
#print(f_ls_kmer)
tup=list(zip(f_ls_kmer,ls_count))
#print(tup)
f1=open(filename+".csv","w")
for i in tup:
    f1.write(i[0])
    f1.write(" ")
    f1.write(i[1])
    f1.write("\n")
f1.close()
    
