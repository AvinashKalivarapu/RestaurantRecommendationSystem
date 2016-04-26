#!/usr/bin/python
import re
import json
f=open("../yelp_academic_dataset_tip.json",'r')
fw=open("tip_features",'w')
fw.write("Format:tip text,business_id,user_id,likes"+"\n")
for line in f:
	data=json.loads(line)
#	cnt=re.sub("[~`!@#$%^&*()_-]",' ',data["text"])
#	cnt=re.sub("[+={}\[\]:>;]",' ',cnt)
#	cnt=re.sub("[',</?*+|\\\".]",' ',cnt)	
	output=str(data["text"].encode('utf-8'))+":"+str(data["business_id"])+":"+str(data["user_id"])+":"+str(data["likes"])+"\n"+"\n"
	print output
	fw.write(output)
	
        
	
 	
