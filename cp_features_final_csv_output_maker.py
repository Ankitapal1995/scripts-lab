from sys import argv
script,filename1,filename2=argv
f1=open(filename1,"r")
union_kmer=[]
for line in f1:
    line=line.strip("\n")
    k=line.split()[0]
    union_kmer.append(k)
#print(union_kmer)
fo=open("feature_ml_union_kmers.csv","w")
for ele in union_kmer:
    fo.write(ele)
    fo.write(",")
fo.write("label")
fo.write("\n")
#for i in range(len(list_f)):
#    for j in list_f[i]:
#        fo.write(str(j))
#        fo.write(",")
#    fo.write("\n")
#fo.write("\n")
fo.close()

