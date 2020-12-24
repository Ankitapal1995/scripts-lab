# read textfile into string 
with open('cat_exap.txt', 'r') as txtfile:
    mytext = txtfile.read()

list_bin=bytearray(mytext)
for i in list_bin:
    l=' '.join(format(i,'b'))
print(l)



# change text into a binary array
#binarray = ' '.join(format(ch, 'b') for ch in bytearray(mytextstring))

# save the file
#with open('cat_exap.bin', 'br+') as binfile:
#    binfile.write(binarray)
