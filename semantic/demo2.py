# -*- coding: utf-8 -*-

"""
Demo program of Hindi WordNet in Python. 

Here I demonstrate all the functionalities of the libraries, but note you can load only the pickle files which are necessary for your task rather than loading every pickle file. Loading of pickle files takes time and memory. But once loaded, all your WordNet operations are just O(1) which means your WordNet lookup is no longer a bottleneck.

Developer: Siva Reddy <siva@sivareddy.in>
Please point http://sivareddy.in/downloads for others to find these python libraries.

"""

import pickle
import sys,ast

word2Synset = pickle.load(open("/home/seecat/experiments/speech/phone_dict_hin/scripts/hindi_wordnet_1.2_python/WordSynsetDict.pk"))
#synset2Onto = pickle.load(open("/home/seecat/experiments/speech/phone_dict_hin/scripts/hindi_wordnet_1.2_python/SynsetOnto.pk"))
synonyms = pickle.load(open("/home/seecat/experiments/speech/phone_dict_hin/scripts/hindi_wordnet_1.2_python/SynsetWords.pk"))
#synset2Gloss = pickle.load(open("/home/seecat/experiments/speech/phone_dict_hin/scripts/hindi_wordnet_1.2_python/SynsetGloss.pk"))
#synset2Hypernyms = pickle.load(open("/home/seecat/experiments/speech/phone_dict_hin/scripts/hindi_wordnet_1.2_python/SynsetHypernym.pk"))
#synset2Hyponyms = pickle.load(open("/home/seecat/experiments/speech/phone_dict_hin/scripts/hindi_wordnet_1.2_python/SynsetHyponym.pk"))
#synset2Hypernyms = pickle.load(open("/home/seecat/experiments/speech/phone_dict_hin/scripts/hindi_wordnet_1.2_python/SynsetHypernym.pk"))
f=open(sys.argv[1],"r")#pos tagged file
mapping={
"WQ": "4",
"NEG" : "4",
"QCC" : "2",
"DEM" : "2",
"JJ" : "2",
"RP" : "4",
"NN" : "1",
"NNC" : "1",
"VAUX" : "3",
"PRP" : "4",
"PSP": "1",
"RB" : "4",
"NSTC" : "1",
"NST" : "4",
"NNP" : "1",
"INTF" : "2",
"RDP" : "1",
"CC" : "1",
"VM" : "3",
"UNK" : "1",
"PRPC" : "2",
"VMC" : "3",
"QC" : "2",
"NNPC" : "1",
"INJ" : "4",
"QF" : "2",
"PSP" : "2",
"JJC" : "2",
"QO" : "2",
"CCC" : "1",
"RBC" : "4",
"QFC" : "2",
"<fs" : "1",
"UNKC" : "1",
"VGF" : "3",
"NULL" : "1",
"SYM" : "1",
"SYMC" : "1",
"XC" : "1"}
w=open(sys.argv[2],"w")
dic={}
#synmap=ast.literal_eval(open(sys.argv[3],"r").readline().replace("\n",""))
for line in f:
	if "<s>" in line or "</s>" in line or line =="\n":
		w.write(line)
		continue
	spl=line.split()
	if len(spl)<3:
		print line 
		continue
	if "PSP" in line:
		pos="1"
	else:
		pos=mapping[spl[1].split(".")[0]]
	word =spl[0].decode("utf-8","ignore")
	root =spl[2].split(".")[0].decode("utf-8","ignore")
	flag=0
	wtup=(word,pos)
	rtup=(root,pos)
#	if wtup in synmap:
#		w.write("syn_"+synmap[wtup]+"\n")
#		flag=-1
#	elif rtup in synmap:
#		w.write("syn_"+synmap[rtup]+"\n")
#		flag=-1
	if word2Synset.has_key(word):
    		synsets1 = word2Synset[word]
    		if  pos in synsets1.keys():
			flag=1
#			for synid in synsets1[pos]:
#				for syno in synonyms[synid][pos]:
					#print syno.encode("utf-8","ignore")
#					synmap[(syno,pos)]=synsets1[pos][0]
#					synmap[synsets1[pos][0]]=syno
	elif word2Synset.has_key(root):
    		synsets2 = word2Synset[root]
    		if  pos in synsets2.keys():
			flag=2
#			for synid in synsets2[pos]:
#				for syno in synonyms[synid][pos]:
#					#print syno.encode("utf-8","ignore")
#					synmap[(syno,pos)]=synsets2[pos][0]
#					synmap[synsets2[pos][0]]=syno
	if flag==0:
		w.write(spl[0]+"\n")
	elif flag==1:
		w.write("syn_"+synsets1[pos][0]+"\n")
		#print synsets1[pos][0]
		if synsets1[pos][0] not in dic:
			dic[synsets1[pos][0]]=[]
		dic[synsets1[pos][0]].append(word)
	elif flag==2:
		w.write("syn_"+synsets2[pos][0]+"\n")
		#print synsets2[pos][0]
		if synsets2[pos][0] not in dic:
			dic[synsets2[pos][0]]=[]
		dic[synsets2[pos][0]].append(word)
open("temp_syn_map","w").write(str(dic))

#open(sys.argv[3],"w").write(str(synmap))		
