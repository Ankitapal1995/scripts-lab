from sys import argv
scripts,filename1,filename2=argv
f1=open(filename1,"r")
kmers_list1=[]
for line in f1:
    line=line.strip("\n")
    l=line.split()[0]
#    g=" ".join(map(str,l))
    kmers_list1.append(l)
#print(kmers_list1)

f2=open(filename2,"r")
important_res=[]
for line in f2:
    line=line.strip("\n")
    l=line.split()
    k=" ".join(map(str,l))
    important_res.append(k)
'''f3=open(filename3,"r")
important_sus=[]
for line in f3:
    line=line.strip("\n")
    l=line.split()
    h=" ".join(map(str,l))
    important_sus.append(h)'''

#print(important_res)
#print(important_sus)
#now prediction for resistant
a=set(kmers_list1)
b=set(important_res)
c=(a & b)
for i in c:
    print(i)
#now prediction for susceptible
#a=set(kmers_list1)
#d=set(important_sus)
#e=(a & d)
#print(len(e))
print (filename1," ",len(c))
