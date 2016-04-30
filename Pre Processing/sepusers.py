import json
f=open("../Datasets/reviews_data.json",'r')
users=[]
for line in f:
	data=json.loads(line)
	users.append(data["user_id"])
f.close()
ff=open("../Generating Features/Feature Files/user_features.txt",'r')
fw=open("../Generating Features/Feature Files/alluserfeatures.txt",'w')
for line in ff:
	user=line.split(",")[0]
	if user in users:
		fw.write(line)
		

ff.close()
fw.close()
		
