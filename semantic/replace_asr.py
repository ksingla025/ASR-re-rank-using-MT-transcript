import sys,re,ast,os,commands,codecs
ls=commands.getstatusoutput("ls "+sys.argv[1])[1].split()#hyp files
asr_dir=sys.argv[2]#asr_syn_map directory
mt_dir=sys.argv[3]#mt_syn_map directory
for fl in ls:	
	if fl[-4:]!=".hyp":
		continue
	print "processing "+fl
	f=open(os.path.join(sys.argv[1],fl),"r").readline().decode("utf-8","ignore")
	dic_asr=ast.literal_eval(open(os.path.join(asr_dir,re.sub(".hyp","_merge_map.txt",fl)),"r").readline().replace("\n",""))
	dic_mt=ast.literal_eval(open(os.path.join(mt_dir,re.sub(".hyp","_map.txt",fl)),"r").readline().replace("\n",""))
	w=codecs.open(os.path.join(sys.argv[4],fl),"w","utf-8")#output directory
	for word in f.split():
		if word[:4]=="syn_":
			if word[4:] in dic_asr:
				set_map=set(dic_asr[word[4:]])
				if len(set_map)>1:
					print "asr",word[4:],
					for x in set_map:
						print x.encode("utf-8","ignore"),
					print "\n",
				w.write(dic_asr[word[4:]][0]+' ')
			elif word[4:] in dic_mt:
				set_map=set(dic_mt[word[4:]])
				if len(set_map)>1:
					print "mt",word[4:],
					for x in set_map:
						print x.encode("utf-8","ignore"),
					print "\n",
				w.write(dic_mt[word[4:]][0]+' ')
			else:
				print "Error: mapping not found for "+word
		else:
			w.write(word+' ')
	w.write("\n")
