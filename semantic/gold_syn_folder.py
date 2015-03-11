#to replace words from string with synset ID
import sys,commands,codecs,re,os
ls=commands.getstatusoutput("ls "+sys.argv[1])[1].split()
mapping={}
for fl in ls:
	open("/home/seecat/integration/scripts/aniruddha/merge_mapping_dic/"+re.sub(".txt","_merge.txt",fl),"w").write(str(mapping))
	if ".txt" not in fl or fl[0]!="P":
		continue
	path = os.path.join(sys.argv[1],fl)
	print 	commands.getstatusoutput("python /home/seecat/integration/scripts/aniruddha/gold_syn_file.py "+path +" /home/seecat/integration/scripts/aniruddha/hn_expanded/"+fl)
