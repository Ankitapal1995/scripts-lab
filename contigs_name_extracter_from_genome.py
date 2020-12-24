from sys import argv
script,filename=argv
import zipfile
zip=zipfile.ZipFile(filename)
list_f=zip.namelist()
mg_ls=[]
for i in list_f:
    f=open(i,"r")
    for line in f:
        line=line.strip("\n")
        if line.startswith(">"):
            mg_ls.append(line)
#print(len(mg_ls))
for i in mg_ls:
    print(i[1:13])
