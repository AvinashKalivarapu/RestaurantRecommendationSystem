#!/usr/bin/python
import json
def decode_json(line):
	try:
		return json.loads(line)
	except:
		return None
if __name__=='__main__':
	with open("../yelp_academic_dataset_business.json") as f:
	 	yelp_data_business = [decode_json(line) for line in f]
	allbusiness=[]
	i=0
	for item in yelp_data_business:
		allbusiness.insert(i,item)
		i=i+1
	j=0
	restaurant=[]
	for item in allbusiness.find({"categories": "Restaurants"}):
		restaurant.insert(j,item)
		j=j+1
	        print item
