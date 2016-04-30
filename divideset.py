import json
from itertools import izip
#f=open('./Generating Features/finalfeatures2.txt','r')
fw=open('./Test/finaltest.txt','w')
fp=open('./test_set.txt','r')
#fk=open('./Datasets/reviews_data.json','r')
k=0
for line in fp:
#	k=k+1
#	if k>90000:
#		fp.write(line)
#	else:
	line=line[46:]
	vv=line.split(",")
	if vv[len(vv)-1].strip("\n")=='Yes':
		ab=1.0
	else:
		ab=0.0
	out=""
	for i in xrange(0,len(vv)-1):
		out=out+vv[i]+","
	out=out+str(ab)  
	fw.write(out+"\n")   
#	data=json.loads(line2)
#	out=data["date"]
#	out2=str(out.split("-")[1])
#	out=str(out.split("-")[0])
#	if out2=='12':
#	  	fp.write(line)
#	else:
#		fw.write(line)

	
#	break
fp.close()
fw.close()

