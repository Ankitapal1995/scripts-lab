#load numpy array from npy file
from numpy import load
from sys import argv
scripts,filename =argv
# load array
data = load(filename)
# print the array
#print(data)
fo=open("important_feature"+filename+".csv","w")
for i in data:
    fo.write(str(i))
    fo.write("\n")
fo.close()
