import linecache
import json
from itertools import izip
f=open("../Code for Labels/reviewlabels.txt",'r')
fw=open("finalfeatures2.txt",'w')
fr=open("./Feature Files/businessallfeatures.txt",'r')
fx=open("../Datasets/reviews_data.json",'r')
fz=open("../Code for Labels/wnscores.txt",'r')
k=1
l=0
rev=0
inf=1
cnt=0
for line,line2,line3 in izip(f,fx,fz):
	cnt=cnt+1
#	print cnt
	dd=json.loads(line2)
	output=""
	jj=1
	while inf==1:
		lineuserfea = linecache.getline("./Feature Files/alluserfeatures.txt",jj)
		if lineuserfea.split(",")[0]==line.split(",")[1]:
			output=output+str(lineuserfea.split(",")[0])+","+str(line.split(",")[0])+","+str(lineuserfea[23:]).strip("\n")+","
			break
		else:
			jj=jj+1


	while inf==1:
#	print "Entered"
		linefea = linecache.getline("./Feature Files/businessallfeatures.txt",k)
#	print linefea
		if linefea.split(",")[0]==line.split(",")[0]:
			output=output+str(linefea[23:]).strip("\n")+","+str(dd["stars"])+","+str(line3.strip("\n"))+","+str(int(dd["votes"]["funny"])+int(dd["votes"]["useful"])+int(dd["votes"]["cool"]))+","+str(line.split(",")[2])
			fw.write(output)
			l=l+1
			break
		else:
			k=k+1
#	if l==2:
#		break
	vv=output.split(",")
	print cnt,":",len(vv)

		

f.close()
fw.close()
fr.close()
		
	
