import json
#f=open("./yelp_academic_dataset_review.json",'r')
fw=open("./dates",'w')
f=open("./only_restaurantsreviews.json",'r')
k=0
rest=[]
#for line in fr:
#	data=json.loads(line)
#	rest.append(data["business_id"])
#print "all restaurants stored\n"
count12=0
count13=0
count14=0
count15=0
cnt11=0
cnt10=0
cnt9=0
months=[0,0,0,0,0,0,0,0,0,0,0,0,0]
''' for line in f:
	k=k+1
	data=json.loads(line)
	out=data["date"]
	out2=str(out.split("-")[1])
	out=str(out.split("-")[0])
#	print out
	if out=="2012":
		count12=count12+1
	if out=="2013":
		count13=count13+1
	if out=="2014":
		count14=count14+1
	if out=="2015":
		count15=count15+1
		ab=int(out2)
	        months[ab]=months[ab]+1
	if out=="2011":
		cnt11=cnt11+1
	if out=="2010":
		cnt10=cnt10+1
	if out=="2009":
		cnt9=cnt9+1

print "2015:",count15,"\n","2014:",count14,"\n","2013:",count13,"\n","2012:",count12,"\n","2011:",cnt11,"\n","2010:",cnt10,"\n","2009:",cnt9	
print "In 2015:"," ",months  '''
for line in f:
	data=json.loads(line)
	out=data["date"]
	out2=str(out.split("-")[1])
	out=str(out.split("-")[0])
	if out=="2015":
		if out2=="


	
f.close()
fw.close()
