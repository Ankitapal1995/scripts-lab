from sys import argv
scripts,filename1,filename2=argv
f1=open(filename1,"r")
f2=open(filename2,"r")
ls_features_name=[]
ls_features_scores=[]
for line in f1:
    line=line.strip("\n")
    ls_features_name.append(line)
for line in f2:
    line=line.strip("\n")
    ls_features_scores.append(line)
#print(ls_features_name)
#print(len(ls_features_name))
#print(ls_features_scores)
#print(len(ls_features_scores))
dict1=dict(zip(ls_features_name,ls_features_scores))
#print(dict1)
#print(len(dict1))

#fo0=open("all_important_features"+filename1[16:35]+".csv","w")
#non_zero_value=[]
#for key in dict1:
#    if dict1[key]!=str(0.0):
#        non_zero_value.append(dict1[key])
#print(non_zero_value)
new_non_zero_dict1={x:y for x,y in dict1.items() if y!=str(0.0)}
#print(new_non_zero_dict1)


fo=open("all_features_score"+filename1[16:35]+".csv","w")
fo.write("total number of features is ")
fo.write(" : ")
fo.write(str(len(dict1)))
fo.write("\n")
for key in dict1:
    fo.write(key)
    fo.write("\t")
    fo.write(dict1[key])
    fo.write("\n")
fo.close()

fo1=open("all_important_features"+filename1[32:37]+".csv","w")
#fo1.write("number of important features")
#fo1.write(":")
#fo1.write(str(len(new_non_zero_dict1)))
#fo1.write("\n")
for key in new_non_zero_dict1:
    fo1.write(key)
    fo1.write("\t")
    fo1.write(new_non_zero_dict1[key])
    fo1.write("\n")
fo1.write("label")
fo1.close()
    
