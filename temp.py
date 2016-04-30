fw=open("./Test/tr.txt",'w')
f=open("./Test/finaltt.txt",'r')
k=0
for line in f:
	fw.write(line)
	line=line.split(",")
	k=k+1
	if k==50000:
		break
#	print len(line)
