fp=open("../Generating Features/finalfeatures2.txt",'r')
avgstars=0.0
avgwnscore=0.0
avgvotes=0.0
k=0
for line in fp:
	k=k+1
	line=line.split(",")
	avgstars=avgstars+float(line[70])
	avgwnscore=avgwnscore+float(line[71])
	avgvotes=avgvotes+float(line[72])
print avgstars/k , " ",avgwnscore/k ," " , avgvotes/k
	
