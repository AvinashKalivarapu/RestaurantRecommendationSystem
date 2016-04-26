#!/usr/bin/python
import json
f = open("../yelp_academic_dataset_business.json",'r')
fw=open("only_restaurants.json",'w')
for line in f:
	data=json.loads(line)
	for item in data["categories"]:
		if "Restaurants" in item:
			fw.write(line)
		elif "Bars" in item:
			fw.write(line)
		elif "Fast Food" in item:
			fw.write(line)
	
        
	
 	
