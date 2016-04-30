from datasetatt import dataset
#from recommendation_data2 import dataset
from math import sqrt
import json
ff=open("../Datasets/onlyrestaurants.json",'r')
allattri=['Accepts Credit Cards', 'Accepts Insurance', 'Alcohol', 'Attire', 'BYOB', 'BYOB/Corkage', 'By Appointment Only', 'Caters', 'Coat Check', 'Corkage', 'Delivery', 'Dogs Allowed', 'Drive-Thru', 'Good For Dancing', 'Good For Groups', 'Good for Kids', 'Happy Hour', 'Has TV', 'Noise Level', 'Open 24 Hours', 'Order at Counter', 'Outdoor Seating', 'Smoking', 'Take-out', 'Takes Reservations', 'Waiter Service', 'Wheelchair Accessible', 'Wi-Fi', 'background_music', 'breakfast', 'brunch', 'casual', 'classy', 'dairy-free', 'dessert', 'dinner', 'divey', 'dj', 'garage', 'gluten-free', 'halal', 'hipster', 'intimate', 'jukebox', 'karaoke', 'kosher', 'latenight', 'live', 'lot', 'lunch', 'romantic', 'soy-free', 'street', 'touristy', 'trendy', 'upscale', 'valet', 'validated', 'vegan', 'vegetarian', 'video']

def similarity_score(person1,person2):
	 
	  # Returns ratio Euclidean distance score of person1 and person2 
	 
	both_viewed = {} # To get both rated items by person1 and person2
	     
	for item in dataset[person1]:
		if item in dataset[person2]:
			both_viewed[item] = 1
				   
				      # Conditions to check they both have an common rating items
	if len(both_viewed) == 0:
		return 0
					      
					         # Finding Euclidean distance
	sum_of_eclidean_distance = [] 
						  
	for item in dataset[person1]:
		if item in dataset[person2]:
			sum_of_eclidean_distance.append(pow(dataset[person1][item] - dataset[person2][item],2))
	sum_of_eclidean_distance = sum(sum_of_eclidean_distance)
	 
	return 1/(1+sqrt(sum_of_eclidean_distance))
	 
def pearson_correlation(person1,person2):
		 
		     # To get both rated items
	both_rated = {}
	for item in dataset[person1]:
		if item in dataset[person2]:
			both_rated[item] = 1
					     
	number_of_ratings = len(both_rated) 
	 
	     # Checking for number of ratings in common
	if number_of_ratings == 0:
		return 0
		       
		           # Add up all the preferences of each user
	person1_preferences_sum = sum([dataset[person1][item] for item in both_rated])
	person2_preferences_sum = sum([dataset[person2][item] for item in both_rated])
	 
	     # Sum up the squares of preferences of each user
	person1_square_preferences_sum = sum([pow(dataset[person1][item],2) for item in both_rated])
	person2_square_preferences_sum = sum([pow(dataset[person2][item],2) for item in both_rated])
	 
	    # Sum up the product value of both preferences for each item
	product_sum_of_both_users = sum([dataset[person1][item] * dataset[person2][item] for item in both_rated])
	 
	   # Calculate the pearson score
	numerator_value = product_sum_of_both_users - (person1_preferences_sum*person2_preferences_sum/number_of_ratings)
	denominator_value = sqrt((person1_square_preferences_sum - pow(person1_preferences_sum,2)/number_of_ratings) * (person2_square_preferences_sum -pow(person2_preferences_sum,2)/number_of_ratings))
	if denominator_value == 0:
		return 0
	else:
		r = numerator_value/denominator_value
		return r 





def user_reommendations(person):

# Gets recommendations for a person by using a weighted average of every other user's rankings
	totals = {}
	simSums = {}
	rankings_list =[]
	for other in dataset:
# don't compare me to myself
		if other == person:
			continue
#		print other
		sim = pearson_correlation(person,other)

# ignore scores of zero or lowera
		if sim <=0:
			continue
		for item in dataset[other]:

# only score movies i haven't seen yet
#			if item not in dataset[person] or dataset[person][item] == 0:
			if item not in dataset[person]:
# Similrity * score
				totals.setdefault(item,0)
				totals[item] += dataset[other][item]* sim
# sum of similarities
				simSums.setdefault(item,0)
				simSums[item]+= sim

# Create the normalized list

	rankings = [(total/simSums[item],item) for item,total in totals.items()]
	rankings.sort()
	rankings.reverse()
# returns the recommended items
	j=0
	li={}
	for score,recommend_item in rankings:
#		print score," ",recommend_item
		if score<0.5:
			score=0
		else:
			score=1
		li[recommend_item]=score
		j=j+1
	for recommend_item in dataset[person]:
#		print recommend_item
		li[recommend_item]=dataset[person][recommend_item]
		j=j+1
#	li=set(li)
#	print len(li)
#	print j
#	print "\n"
#recommendataions_list = [recommend_item for score,recommend_item in rankings]
	return li
k=0
ds={}
fw=open("./businessallfeatures2.txt",'w')
for line in ff:
	data=json.loads(line)
#	print data['business_id']
	ds={}	
	ds=user_reommendations(data['business_id'])
	fw.write(data['business_id'])
	cnt=0
	if len(ds)!=61:
		for i in allattri:
			if i not in ds.keys():
				cnt=cnt+1
				fw.write(","+"0")
			else:
			 	cnt=cnt+1
			 	fw.write(","+str(ds[i]))
	else:
		for i in allattri:
			cnt=cnt+1
			fw.write(","+str(ds[i]))
#			temp.append(i)

#	print "\n"
        fw.write(","+str(data["stars"])+","+str(data["review_count"]))
	fw.write("\n")
	k=k+1
	print k,":",cnt	 
	
	
ff.close()
fw.close()
