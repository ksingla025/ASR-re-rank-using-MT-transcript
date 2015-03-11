import sys,commands,os,re
#to replace words in MT lattice with synset id
ls=commands.getstatusoutput("ls "+sys.argv[1])[1].split()# folder in which there aare lattices
for fl in ls:
	if ".txt" not in fl or fl[0]!="P" or "syn" in fl:
		continue
	print fl
	mapping={}
	print commands.getstatusoutput("python posfile.py "+os.path.join(sys.argv[1],fl)+" temp")
	open("/home/seecat/integration/scripts/aniruddha/merge_mapping_dic/"+re.sub(".txt","_merge.txt",fl),"w").write(str(mapping))
	print commands.getstatusoutput("python demo.py hindi.sample.out.txt  temp "+"/home/seecat/integration/scripts/aniruddha/merge_mapping_dic/"+re.sub(".txt","_merge.txt",fl))
	print commands.getstatusoutput("mv  temp_syn_map  mt_syn_mapping/"+re.sub(".txt","_map.txt",fl))
	print commands.getstatusoutput("sh commands1.sh  temp temp1")
	print commands.getstatusoutput("python join.py  "+os.path.join(sys.argv[1],fl)+ " temp1 " +os.path.join(sys.argv[1],re.sub(".txt","_syn.txt",fl)))
