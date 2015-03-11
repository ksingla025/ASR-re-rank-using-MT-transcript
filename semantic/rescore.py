import os,sys,commands,re
#sys.argv[1] : path to directory containing final hypotheses with synset IDs ( Example data_artificial_29_merge_syns)
#sys.argv[2] : path to directory containing asr lattices with and without synset IDs (ex. P01_T1_S1_asr.txt, P01_T1_S1_syn.txt)
#sys.argv[3] " path to output directory
commands.getstatusoutput("mkdir "+sys.argv[3])
ls=commands.getstatusoutput("ls "+sys.argv[1])[1].split()
for x in ls:
	hyp = open(os.path.join(sys.argv[1],x),"r").readline().split()
	asr_lat=[[]]
	syn_lat=[[]]
	asr=open(os.path.join(sys.argv[2],re.sub(".hyp","_asr.txt",x)),"r")
	syn=open(os.path.join(sys.argv[2],re.sub(".hyp","_syn.txt",x)),"r")
	for line in asr:
		spl=line.split()
		if len(spl)>=4:
			asr_lat[-1].append(spl[2])
		else:
			asr_lat.append([])
	count=0
	flag=0
	for line in syn:
		spl=line.split()
		if len(spl)>=4:
			syn_lat[-1].append(spl[2])
		else:
			if syn_lat[-1]==hyp:
				flag=1
				w=open(os.path.join(sys.argv[3],x),"w")
				w.write(" ".join(asr_lat[count])+"\n")
				w.close()
				break
			else:
				count+=1
				syn_lat.append([])
	if flag==0:
		print " ".join(hyp)
		for z in syn_lat:
			print " ".join(z)
		print "-"*45
