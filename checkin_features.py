#!/usr/bin/python
import re
import json
f=open("../yelp_academic_dataset_checkin.json",'r')
fw=open("checkin_features",'w')
fw.write("Format:business_id,checkin_info"+"\n")
for line in f:
	data=json.loads(line)	
	output=str(data["business_id"])+","+str(data["checkin_info"])+"\n"
	print output
	fw.write(output)
	
        
	
 	
