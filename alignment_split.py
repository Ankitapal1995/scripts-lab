from sys import argv
scripts,filename=argv
f=open(filename,"r")
n=f.readlines()
begin_ls=[]
end_ls=[]
line_ls=[]
for line in n:
    if line.startswith("-- BEGIN"):
        begin_ls.append(n.index(line))
    elif line.startswith("--   END"):
        end_ls.append(n.index(line))
    else:
        line_ls.append(line)
print(begin_ls)
print(end_ls)
#print(line_ls)
tup1=list(zip(begin_ls,end_ls))
print(tup1)

for i in tup1:
    fo=open(filename[:-7]+"_"+str(tup1.index(i))+".csv","w")
    for j in range(i[0],(i[1]+1)):
        fo.write(n[j])
    fo.close()


