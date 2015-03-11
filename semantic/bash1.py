import sys,commands,os,re
print commands.getstatusoutput("python /home/seecat/integration/scripts/aniruddha/posfile.py "+sys.argv[1]+" temp_ani")
print commands.getstatusoutput("python /home/seecat/integration/scripts/aniruddha/demo.py hindi.sample.out.txt  temp "+sys.argv[2])
print commands.getstatusoutput("mv  temp_syn_map  /home/seecat/integration/scripts/aniruddha/asr_syn_mapping/"+re.sub(".txt","_map.txt",os.path.basename(sys.argv[2])))
print commands.getstatusoutput("sh /home/seecat/integration/scripts/aniruddha/commands1.sh  temp temp1")
print commands.getstatusoutput("python /home/seecat/integration/scripts/aniruddha/join.py  "+sys.argv[1]+ " temp1 " +re.sub(".txt","_syn.txt",sys.argv[1]))
