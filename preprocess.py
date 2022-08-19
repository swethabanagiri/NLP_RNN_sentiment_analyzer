import json
from collections import Counter
from nltk.corpus import stopwords
import re


def preprocess(file,num,offset=0):									#num = total number of tweets to consider
	stri=""															#offset = initial tweet to consider for training/testing
	stop = set(stopwords.words('english'))
	print len(file['root'])
	for i in range(offset,(num+offset)):								
		string=file['root'][i]['text'].encode('ascii','ignore')			#Getting tweet by tweet from text
		k = [j for j in string.lower().split() if j not in stop]		#Removing stop words
		for l in k:
			cleanString = re.sub('\W+',' ', l )							#clean string if it has special characters or numbers
			l.replace(l,cleanString)
		strin=' '
		for h in k:
			strin+=h+' '
		stri+=strin+'\n'
	return stri

#For training	
with open("neg_amazon_cell_phone_reviews.json",'r') as f :
	file=json.loads(f.read())
	neg_stri = preprocess(file,1000)
	with open('train_processed.txt','w') as w:
		w.write(str(neg_stri)+'\n\n\n\n')

with open("pos_amazon_cell_phone_reviews.json",'r') as f :
	file=json.loads(f.read())
	pos_stri = preprocess(file,1000)
	with open('train_processed.txt','a') as w:	
		w.write(str(pos_stri)+'\n\n\n\n')

#For testing
with open("neg_amazon_cell_phone_reviews.json",'r') as f :
	file=json.loads(f.read())
	pos_stri = preprocess(file,100,1000)
	with open('test_processed.txt','w') as w:
		w.write(str(pos_stri)+'\n\n\n\n')


with open("pos_amazon_cell_phone_reviews.json",'r') as f :
	file=json.loads(f.read())
	pos_stri = preprocess(file,100,1000)
	with open('test_processed.txt','a') as w:
		w.write(str(pos_stri)+'\n\n\n\n')
