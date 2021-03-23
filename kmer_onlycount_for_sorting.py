from sys import argv
script,filename,k=argv       #argument for input file and given k value
outputfile=('kmer'+k+'.csv') #argument for output csv file
k=int(k)                     #convert input k value into integer
n=open(filename)             #open of input file
read_line=n.readlines()                              #list of line by reading each lines
#print(f"list of line:{read_line}")
list_of_line=[x.upper()for x in read_line]            #convert into upper_case
#print(f"modified uppercase line:{list_of_line}")
sequence_only_list=[]
for line in list_of_line:
    if line.startswith(">",0):
        a=2
    else:
      sequence_only_list.append(line.strip())
#print(f"final sequence list{sequence_only_list}")
dna=''.join(sequence_only_list)
#print(dna)
out=[(dna[i:i+k])for i in range (0,(len(dna)-k+1))]
for j in out:
    print(j)

