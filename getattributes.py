import json
f=open("./only_restaurants.json",'r')
fw=open("./attributes",'w')
att={}
for line in f:
	data=json.loads(line)
	att.clear()
	out=""
	out=str(data["business_id"])
	for key,value in data["attributes"].iteritems():
		 if type(value) is dict:
			 for i,j in value.iteritems():
				  if type(j) is bool:
				  	if j==True:
						att[i]=1
					else:   
					        att[i]=0
				  else:
				  	if i=="Alcohol":
				        	if j=="none":
				                	att[i]=0
				           	else:   
				                   	att[i]=1
				   	elif i=="Noise Level":
				        	if j=="very_loud" or j=="loud":
				                	att[i]=1
				           	else:   
				                   	att[i]=0
				   	elif i=="Attire":
				           	if j=="casual":
				                	att[i]=0
				           	else:   
				                   	att[i]=1
				   	elif i=="Smoking":
				           	if j=="no":
				                	att[i]=0
				           	else:
				                	att[i]=1
				   	elif i=="Wi-Fi":
				           	if j=="no":
				                	att[i]=0
				          	else:
				                	att[i]=1
				   	elif i=="BYOB/Corkage":
				        	if j=="no":
				                	att[i]=0
				           	else:
				   			att[i]=1
		 else:
		 	if type(value) is bool:
				if value== True:
					att[key]=1
				else:
					att[key]=0
			else:
			 	if key=="Alcohol":
			 		if value=="none":
			 			att[key]=0
			 		else:
			 			att[key]=1
			 	elif key=="Noise Level":
			 		if value=="very_loud" or value=="loud":
			 			att[key]=1
			 		else:
			 			att[key]=0
			 	elif key=="Attire":
			 		if value=="casual":
			 			att[key]=0
			 		else:
			 			att[key]=1
			 	elif key=="Smoking":
			 		if value=="no":
			 			att[key]=0
			 		else:
			 			att[key]=1
			 	elif key=="Wi-Fi":
			 		if value=="no":
			 			att[key]=0
			 		else:
			 			att[key]=1
			 	elif key=="BYOB/Corkage":
			 		if value=="no":
			 			att[key]=0
			 		else:
			 			att[key]=1
		
	for k,v in att.iteritems():
		out=out+","+str(k)+":"+str(v)
#	out=out+"\n"
	print out
#	fw.write(out)
#	break
f.close()
fw.close()
