import commands,os,sys
#arg1=directory containing final hypo with syn IDs
#arg2=directory containing all asr hypo with syn
#arg3=directory containing all asr hypo without syn
#arg4=output dir
ls=commands.getstatusoutput("ls "+sys.argv[1])[1].split()
for f in ls:
	if ".txt" not in f or f[0]!="P":
		continue
	src=open(os.path.join(sys.argv[1],f),"r").readline().split()
	hyp=-1
	i=-1
	for line in open(os.path.join(sys.argv[2],f),"r"):
		i+=1
		tgt=line.split()
		if src==tgt:
			hyp=i
			break
	print f,hyp
	open(os.path.join(sys.argv[4],f),"w").write(open(os.path.join(sys.argv[3],f),"r").readlines()[hyp])
	if hyp==-1:
		print "not found",f,src
