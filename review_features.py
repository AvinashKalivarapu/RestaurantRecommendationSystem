#!/usr/bin/python
import json
f=open("../yelp_academic_dataset_review.json",'r')
fw=open("review_features",'w')
fw.write("Format:business_id,user_id,stars,funny,useful,cool"+"\n")
for line in f:
	data=json.loads(line)
	output=str(data["business_id"])+","+str(data["user_id"])+","+str(data["stars"])+","
	votes=str(data["votes"]).split(":")
	output=output+str(votes[1].split(",")[0]).strip(" ")+","  #funny
	output=output+str(votes[2].split(",")[0]).strip(" ")+"," #useful
	output=output+str(votes[3].strip("}")).strip(" ")+"\n" #cool
	print output
	fw.write(output)
	
        
	
 	
