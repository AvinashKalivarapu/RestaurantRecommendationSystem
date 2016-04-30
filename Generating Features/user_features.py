#!/usr/bin/python
import json
import sys
from datetime import datetime
def raw_features(filename):
	 data=[]
	 buff=[]
	 f = open(filename, 'r' )
	 fw=open("user_features.txt",'w')
#	 fw.write("Format: userid,review_count,average_stars,funny,useful,cool,yelping_since,no of fans"+"\n")
	 i=0;
	 for line in f:
#  data.append(json.loads(line))
		   data=line.split(":")
		   userid = data[8].split(",")[0]
		   userid=userid.replace('\"','') #userid
		   output=userid.strip(" ")+","
		   output=output+str(data[6].split(",")[0]).strip(" ")+"," #review_count
		   output=output+str(data[11].split(",")[0]).strip(" ")+","#average_stars
#		   output=output+str(data[3].split(",")[0]).strip(" ")+"," #votes_funny
#		   output=output+str(data[4].split(",")[0]).strip(" ")+"," #votes_useful
#		   output=output+str(data[5].split(",")[0].strip('}')).strip(" ")+"," #votes_cool
		   totalvotes=int(str(data[3].split(",")[0]).strip(" "))+int(str(data[3].split(",")[0]).strip(" "))+int(str(data[5].split(",")[0].strip('}')).strip(" "))
		   output=output+str(totalvotes)+","
		   datee=str(str(data[1]).split(",")[0].replace('\"','')) #yelpingsince
		   d1 = datetime.strptime(datee.strip(" "),"%Y-%m")
		   d2 = datetime.strptime("2016-04", "%Y-%m")
		   output=output+str(abs((d1-d2).days)).strip(" ")+","
		   output=output+str(data[10].split(",")[0]).strip(" ")+"\n"#no of fans
                   fw.write(output)
                   print output
		   
		   
	 fw.close()
	 f.close()


if __name__ == '__main__':
 	raw_features(sys.argv[1])
 	
