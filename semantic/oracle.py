import sys,commands,os
ls=commands.getstatusoutput("ls "+sys.argv[1])[1].split()
for f in ls:
	if f[0]!="P" or ".txt" not in f:
		continue
	spl=open(os.path.join(sys.argv[1],f),"r").readline().split()
	w=open(os.path.join(sys.argv[2],f),"w")
	for word in spl:
		w.write("0 0 "+word+" "+word+"\n")
	w.write("0\n")

