import sys,re,commands
f=open(sys.argv[1],"r").readlines()#xliff input file
src=f[0][:-1]
tgt=f[1][:-1]
for line in f[2:]:
	spl=line.split()
        sid=spl[0]
        src_str=" ".join(spl[1:])
        print  sid,"\n",src_str
	#print src,tgt
        if src=="en" and tgt=="hi":
            commands.getstatusoutput("echo \""+src_str+"\"|/srv/tools/mosesdecoder/bin/moses -f /home/seecat/MT/experiments/baseline_180k/working-dir/moses.tuned.ini.1 -n-best-list /home/seecat/integration/data/precompute_mt/text_"+sid+"_hyp.txt 10")
	    commands.getstatusoutput("python /home/seecat/integration/scripts/mt_lattice2.py /home/seecat/integration/data/precompute_mt/text_"+sid+"_hyp.txt  /home/seecat/integration/data/precompute_mt/text_"+sid+".txt 10")
        if src=="en" and tgt=="es":
            commands.getstatusoutput("echo \""+src_str+"\"|/srv/tools/mosesdecoder/bin/moses -f /home/seecat/MT/experiments/eng-span/working-dir/moses.tuned.ini.1 -n-best-list /home/seecat/integration/data/precompute_mt/text_"+sid+"_hyp.txt 10")
	    commands.getstatusoutput("python /home/seecat/integration/scripts/mt_lattice2.py /home/seecat/integration/data/precompute_mt/text_"+sid+"_hyp.txt  /home/seecat/integration/data/precompute_mt/text_"+sid+".txt 10")
