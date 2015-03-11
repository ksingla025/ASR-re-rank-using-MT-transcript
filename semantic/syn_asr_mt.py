import sys,re,os,commands
folder=sys.argv[1]
import threading
import logging
import time
ls=commands.getstatusoutput("ls "+folder)[1].split()
for fl in ls:
	if ".wav" in fl:
		print fl
		print commands.getstatusoutput("python /home/seecat/integration/scripts/hindi_syn_merge.py "+os.path.join(folder,fl)+" tt "+"/home/seecat/integration/scripts/aniruddha/merge_mapping_dic/"+re.sub(".wav","_merge.txt",fl))
		print "see",commands.getstatusoutput("mv tt /home/seecat/integration/scripts/aniruddha/data_67_combine_first_syns/"+re.sub(".wav",".hyp",fl))
