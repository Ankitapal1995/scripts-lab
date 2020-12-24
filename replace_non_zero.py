from sys import argv
script,filename=argv
f=open(filename,'r')
ls_line=[]
for line in f:
    line =line.strip("\n")
    ls_line.append(line)
#    l=line.split(",")
#    ls_value.append(l)
#print(l)
#print(ls_line)
ls_value=[]
for i in ls_line:
    l=i.split(",")
    ls_value.append(l)
print(ls_value)
ls_new_val=[]
def replace_value(k):
    for n in range(0,(len(k)-1)):
        ls_new_val.append(k[n])


for i in ls_value:
    replace_value(i)
print(ls_new_val)

#for h in range(0,(len(ls_new_val)-1)):
#    if ls_new_val[h]!=0:
#        ls_new_val[h]=1
#    else:
#        ls_new_val[h]=0
#    print(ls_new_val)

