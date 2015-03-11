import sys,codecs
f1=open(sys.argv[1],"r").readlines()#lattice file
f2=open(sys.argv[2],"r").readlines()#synset file
w=codecs.open(sys.argv[3],"w","utf-8")#final lattice with synsets  Ids
for i in range(len(f1)):
	line1=unicode(f1[i].decode("utf-8","replace"))
	if i <len((f2)):
		line2=unicode(f2[i].decode("utf-8","replace"))
	else:
		line2=""
	spl1=line1.split()
	spl2=line2.split()
	if len(spl1)>=4:
		spl1[2]=spl2[0]
		spl1[3]=spl2[0]
	w.write(" ".join(spl1)+"\n")
