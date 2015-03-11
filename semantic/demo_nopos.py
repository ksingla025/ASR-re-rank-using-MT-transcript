# -*- coding: utf-8 -*-


"""
Demo program of Hindi WordNet in Python. 

Here I demonstrate all the functionalities of the libraries, but note you can load only the pickle files which are necessary for your task rather than loading every pickle file. Loading of pickle files takes time and memory. But once loaded, all your WordNet operations are just O(1) which means your WordNet lookup is no longer a bottleneck.

Developer: Siva Reddy <siva@sivareddy.in>
Please point http://sivareddy.in/downloads for others to find these python libraries.

"""

import pickle
import sys,ast
import codecs
word2Synset = pickle.load(open("/home/seecat/experiments/speech/phone_dict_hin/scripts/hindi_wordnet_1.2_python/WordSynsetDict.pk"))
#synset2Onto = pickle.load(open("/home/seecat/experiments/speech/phone_dict_hin/scripts/hindi_wordnet_1.2_python/SynsetOnto.pk"))
synonyms = pickle.load(open("/home/seecat/experiments/speech/phone_dict_hin/scripts/hindi_wordnet_1.2_python/SynsetWords.pk"))
#synset2Gloss = pickle.load(open("/home/seecat/experiments/speech/phone_dict_hin/scripts/hindi_wordnet_1.2_python/SynsetGloss.pk"))
#synset2Hypernyms = pickle.load(open("/home/seecat/experiments/speech/phone_dict_hin/scripts/hindi_wordnet_1.2_python/SynsetHypernym.pk"))
#synset2Hyponyms = pickle.load(open("/home/seecat/experiments/speech/phone_dict_hin/scripts/hindi_wordnet_1.2_python/SynsetHyponym.pk"))
#synset2Hypernyms = pickle.load(open("/home/seecat/experiments/speech/phone_dict_hin/scripts/hindi_wordnet_1.2_python/SynsetHypernym.pk"))
f=open(sys.argv[1],"r")#sentence file
w=codecs.open(sys.argv[2],"w","utf-8")#synset sentences
dic={}
synmap={}
for line in f:
    if line=="" or line =="\n":
	w.write(line)
	continue
    line=line.decode("utf-8","ignore")
    spl=line.split()
    for word in spl:
	flag=0
	wtup=word
	if wtup in synmap:
		w.write("syn_"+synmap[wtup]+" ")
		if synmap[wtup] not in dic:
			dic[synmap[wtup]]=[]
		dic[synmap[wtup]].append(word)
		flag=-1
	elif word2Synset.has_key(word):
    		synsets1 = word2Synset[word]
		pos1=synsets1.keys()[0]
    		for  pos in synsets1.keys():
			flag=1
			for synid in synsets1[pos]:
				for syno in synonyms[synid][pos]:
					#print syno.encode("utf-8","ignore")
					synmap[syno]=synsets1[pos1][0]
					synmap[synsets1[pos1][0]]=syno
			if synsets1[pos1][0] not in dic:
				dic[synsets1[pos1][0]]=[]
			dic[synsets1[pos1][0]].append(word)
	if flag==0:
		w.write(word+" ")
	elif flag==1:
		w.write("syn_"+synsets1[pos1][0]+" ")
		print synsets1[pos1][0]
		if synsets1[pos1][0] not in dic:
			dic[synsets1[pos1][0]]=[]
		dic[synsets1[pos1][0]].append(word)
    w.write("\n")
open("temp_syn_map","w").write(str(dic))

open(sys.argv[3],"w").write(str(synmap))		
