fp=open('./attributes.txt','r')
fw=open('./datasetatt.py','w')
dataset={}
temp={}
k=0
for line in fp:
	data=line.split(",")
	temp={}
	for i in xrange(1,len(data)):
		key=data[i].split(":")[0]
		key=key.strip("\n")
		temp[key]=int(data[i].split(":")[1].strip("\n"))
#	dataset[data[0]]={}
#	print data[0]
	dataset[data[0].strip("\n")]=temp
#	print dataset

#print temp
#print dataset
fw.write(str(dataset))
fw.close
fp.close()


