# -*- coding: utf-8 -*-

"""
Demo program of Hindi WordNet in Python. 

Here I demonstrate all the functionalities of the libraries, but note you can load only the pickle files which are necessary for your task rather than loading every pickle file. Loading of pickle files takes time and memory. But once loaded, all your WordNet operations are just O(1) which means your WordNet lookup is no longer a bottleneck.

Developer: Siva Reddy <siva@sivareddy.in>
Please point http://sivareddy.in/downloads for others to find these python libraries.

"""

import pickle,sys,commands,os,copy,codecs

#word2Synset = pickle.load(open("WordSynsetDict.pk"))
#synset2Onto = pickle.load(open("SynsetOnto.pk"))
synonyms = pickle.load(open("/home/seecat/experiments/speech/phone_dict_hin/scripts/hindi_wordnet_1.2_python/SynsetWords.pk"))
#synset2Gloss = pickle.load(open("SynsetGloss.pk"))
#synset2Hypernyms = pickle.load(open("SynsetHypernym.pk"))
#synset2Hyponyms = pickle.load(open("SynsetHyponym.pk"))
#synset2Hypernyms = pickle.load(open("SynsetHypernym.pk"))
ls=commands.getstatusoutput("ls "+sys.argv[1])[1].split()#input folder
out=sys.argv[2]#output folder
for fl in ls:
	path = os.path.join(sys.argv[1],fl)
	line=open(path,"r").readline().decode("utf-8","ignore")
	w=codecs.open(os.path.join(out,fl),"w","utf-8")
	spl=line.split()
	lst=[[]]
	for word in spl:
		if "syn_" not in word:
			for x in lst:
				x.append(word)
		else:
			lst1=[]
			for y in lst:
				print synonyms[word[4:]]
				pos=synonyms[word[4:]].keys()[0]
				for x in synonyms[word[4:]][pos]:
					tmp=copy.deepcopy(y)
					tmp.append(x)
					lst1.append(tmp)
			lst=lst1
	for x in lst:
		w.write(" ".join(x)+"\n".encode("utf-8","ignore"))
		
		
