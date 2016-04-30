import json
import re
import sys
import nltk
from DictionaryBuilder import *

sys.path.insert(0,'ark-tokenizer')
from ark import tokenizeRawTweetText

ed=getEmoticonDictionary()
ad=getAcronymDictionary()
swd=getStopwordDictionary()
wn_dict=getWordnetDictionary()

def replaceRepetition(review):
    for i in range(len(review)):
        x=list(review[i])
        if len(x)>3:
            flag=0
            for j in range(3,len(x)):
                if(x[j-3]==x[j-2]==x[j-1]==x[j]):
                    x[j-3]=''
                    if flag==0:
                        flag=1
            review[i]=''.join(x).strip(specialChar)
    return review

def removeNonEnglishWords(review):
    newReview=[]
    for i in range(len(review)):
        if review[i]!='':
            chk=re.match(r'([a-zA-z0-9 \+\?\.\*\^\$\(\)\[\]\{\}\|\\/:;\'\"><,.#@!~`%&-_=])+$',review[i])
            if chk:
                newReview.append(review[i])
    return newReview

def removeStopWords(stopWordsDict,review):        
    newReview=[]
    for i in range(len(review)):
        if review[i].strip(specialChar) not in stopWordsDict:
            newReview.append(review[i])
    return newReview

def replaceEmoticons(emoticonsDict,review):
    for i in range(len(review)):
        if review[i] in emoticonsDict:
            review[i]=emoticonsDict[review[i]]
    return review


def expandAcronym(acronymDict,review):
    newReview=[]
    for i in range(len(review)):
        word=review[i].strip(specialChar)
        if word:
            if word in acronymDict:
                newReview+=acronymDict[word].split(" ")
            else:
                newReview+=[review[i]]
    return newReview

def expandNegation(review):
    newReview=[]
    for i in range(len(review)):
        word=review[i].strip(specialChar)
        if(word[-3:]=="n't"):
            if word[-5:]=="can't" :
                newReview.append('can')
            else:
                newReview.append(word[:-3])
            newReview.append('not')
        else:
            newReview.append(review[i])
    return newReview

def replaceNegation(review):
    for i in range(len(review)):
        word=review[i].lower().strip(specialChar)
        if(word=="no" or word=="not" or word.count("n't")>0):
            review[i]='negative'
    return review

def replaceURL(review):
    review=re.sub('((www\.[^\s]+)|(https?://[^\s]+))','',review)
    return review

def replaceTarget(review):
    review=re.sub('@[^\s]+','',review)
    return review

def removeNumbers(review):
    review=re.sub('^[0-9]+', '', review)
    return review

def replaceHashtag(review):
    review=re.sub(r'#([^\s]+)', r'\1', review)
    return review

def mergeSpace(review):
    return re.sub('[\s]+', ' ', review)

def processReview(review,ed,ad,swd):
    
    review=review.lower()
    review = replaceURL(review)
    review = replaceTarget(review)
    review = replaceHashtag(review)
    
    review = mergeSpace(review)
    review = review.strip('\'"')
    review = review.strip(' ')
    review = review.split(" ")
	   
    review = removeNonEnglishWords(review)
    review = replaceRepetition(review)
    review = replaceEmoticons(ed,review)
    review = expandAcronym(ad,review)
    
    review = expandNegation(review)
    review = replaceNegation(review)
    
    review = removeStopWords(swd,review)
    for i in xrange(len(review)-1,-1,-1):
        if review[i] == '':
            review.pop(i)
    
    review = " ".join(review)
    tokenizedReview=tokenizeRawTweetText(review)
    review_size=len(tokenizedReview)
    wn_score=0
    for j in range(review_size):
        if tokenizedReview[j] in wn_dict:
            wn_score+=wn_dict[tokenizedReview[j]]

    return wn_score

if __name__=='__main__':
	f = open('../Datasets/reviews_data.json','r')
	fw= open('./wnscores.txt','w')
	k=0
	for line in f:
		data=json.loads(line)
		wn_score=processReview(data["text"],ed,ad,swd)
#		rating=data["stars"]
#		if wn_score < 0:
#			if rating > 4 :
#		        	label="Yes"
#			else:
#				label="No"
#		elif wn_score >= 0:
#			if rating > 3:
#				label="Yes"
#			else: 
#				label="No"
#		out = str(data['business_id'])+","+str(data['user_id'])+","+label+"\n" 
		out=str(wn_score)+"\n"
		fw.write(out)
		k=k+1
#		print label,":",k
		print k
	f.close()
	fw.close()
