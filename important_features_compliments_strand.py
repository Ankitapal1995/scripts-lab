from sys import argv
script,filename=argv
f=open(filename,"r")
ls=[]
for line in f:
    line=line.strip("\n")
    ls.append(line)
##########rev_comp####
rev={"A":"T","T":"A","G":"C","C":"G"}
def comp_rev(x):
    ls_rev=[]
    y=x[::-1]
    for i in y:
        ls_rev.append(rev[i])
        str1="".join(ls_rev)

    #    h=j[::-1]
    return str1 
rev_comp=[]
for i in ls:
    j=comp_rev(i)
    rev_comp.append(j)
#######
fo=open(filename+"comp.csv","w")
for i in rev_comp:
    fo.write(">fasta"+str(rev_comp.index(i)))
    fo.write("\n")
    fo.write(i)
    fo.write("\n")
fo.close()



