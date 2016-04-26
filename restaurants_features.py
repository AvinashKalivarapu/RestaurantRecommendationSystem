#!/usr/bin/python
import json
f=open("../only_restaurants.json",'r')
fw=open("restaurant_features",'w')
at=[]
maa=-1
g=0
sub=[]
boolean=[]
nonboolean=[]
nonbooleanvalues={}
for line in f:
	data=json.loads(line)
#	output=str(data["business_id"])+","+str(data["full_address"].replace("\n"," ").encode('utf-8'))+","+str(data["city"].encode('utf-8'))+","+str(data["state"].encode('utf-8'))+","+str(data["stars"])+","+str(data["review_count"])+","+str(data["attributes"])+"\n"
	k=0
	for key,value in data["attributes"].iteritems():
		if type(value) is dict:
			for i,j in value.iteritems():
				if type(j) is bool:
					boolean.append(i)
				else:
					try:
						ab=list(nonbooleanvalues[i])
						ab.append(j)
						nonbooleanvalues[i]=set(ab)
					except:
						ab=[]
						ab.append(j)
						nonbooleanvalues[i]=set(ab)
			sub.extend(value.keys())
		else:
			if type(value) is bool:
				boolean.append(key)
			else:
				try:
					ab=list(nonbooleanvalues[key])
					ab.append(value)
					nonbooleanvalues[key]=set(ab)
				except:
					ab=[]
					ab.append(value)
					nonbooleanvalues[key]=set(ab)
#				nonboolean.append(key)
			sub.append(key)

#at = set(at)
#print "Count of all attributes ",len(at)
sub=set(sub)
boolean=set(boolean)
print sub
print "Count Of all attributes ",len(sub)
print boolean
print "Count Of all boolean attributes",len(boolean)
nonboolean=set(nonboolean)
print nonbooleanvalues
#print "Count of all nonboolean attributes",len(nonboolean)

	
#	fw.write(output)
	
        
	
 	
