import json
f=open("only_restaurants.json",'r')
fw=open("onlyrestaurants.json",'w')
d={}
for line in f:
	data=json.loads(line)
	try:
		t=d[data["business_id"]]
	except:
		d[data["business_id"]]=1
		fw.write(line)

fw.close()
f.close()



