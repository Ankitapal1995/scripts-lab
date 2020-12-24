from sys import argv
script,filename=argv       #argument for input file and given k value
#outputfile=('kmer'+k+'.csv') #argument for output csv file              #convert input k value into integer
n=open(filename)             #open of input file
read_line=n.readlines()                              #list of line by reading each lines
#print(f"list of line:{read_line}")
list_of_line=[x.upper()for x in read_line]
list_of_line_1=[]
for i in list_of_line:
    j=i.replace("N","")
    list_of_line_1.append(j)
#print(list_of_line_1)
#convert into upper_case
#print(f"modified uppercase line:{list_of_line}")
sequence_only_list=[]
header_list=[]
for line in list_of_line_1:
    if line.startswith(">",0):
        header_list.append(line)
    else:
      sequence_only_list.append(line.strip())
#print(header_list)
#print(sequence_only_list)
dna=''.join(sequence_only_list)

n=80
chunks=[dna[i:i+n]for i in range(0,len(dna),n)]
#print(chunks)
#out=[(dna[i:i+k])for i in range (0,(len(dna)-k+1))]
#for j in out:
#    print(j)
file_name=filename.rsplit(".1",1)[0]
header=">"+filename
#print(header)
fo=open(file_name+".txt","w")
fo.write(header)
fo.write("\n")
for i in chunks:
    fo.write(str(i))
    fo.write("\n")
fo.close()
