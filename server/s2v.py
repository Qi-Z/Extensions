import os
import nltk
import re
import numpy as np
import pickle
from nltk.stem.snowball import SnowballStemmer


def gen_feature_test(sent, retval):
	# header = 
	stemmer = SnowballStemmer("english")
	unigrams = ["skin", "room", "hotel", "clean", "easi", "servic", "stay", "breakfast", "love","place","best","product","one","recommend","veri","food","definit","look","tri", "didnt",  "onli", "color", "face", "dont", "even", "old", "price", "tast", "disappoint","worst","bad","never","money"]
	uni_indx = np.zeros(len(unigrams))
	totalWordCnt = 0
	coordinatingConjunctions = 0
	NNCnt = 0
	sent = re.sub("(')", "", sent)
	sent = re.sub("\\W+", " ", sent)
	sent = sent.lower()


	s = nltk.word_tokenize(sent)


	# print s
	totalWordCnt = len(s)

	for token in s:
		if re.match(token, "and|nor|but|or|yet|so|for"):
			coordinatingConjunctions+=1
		token  = stemmer.stem(token)
		# print token
		if token in unigrams:
			uni_indx[unigrams.index(token)]+=1
	# print uni_indx
	tokenized_s = nltk.pos_tag(s)
	for token in tokenized_s:
		if token[1] == "NN":
			NNCnt+=1


	feature_vect =  np.array([totalWordCnt, coordinatingConjunctions, NNCnt])
	
	
	retval.append(list(feature_vect) + list(uni_indx))
	# outf = ""
	# for i in feature_vect:
	# 	outf+= str(i) + ','

	# for i in range(len(uni_indx)):
	# 	if i == len(uni_indx) -1:
	# 		outf+= str(uni_indx[i])
	# 	else:
	# 		outf+=str(uni_indx[i]) + ','
	# # outf+='\n'
	# retval.append(outf)
	return retval

# ret = []
# gen_feature_test("I am very happy! nice product", ret)
# print ret
