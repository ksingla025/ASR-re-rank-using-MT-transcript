#!/usr/bin/python

import sys
import re
import os,commands

participants = 1
tasks = 4
sentences = 10
file_opened_hyp = {}
file_opened_ref = {}
lines = {}

file_complete_hyp=open("./karan/complete_hyp.txt","w")
file_complete_ref=open("./karan/complete_ref.txt","w")
for j in range(1,tasks+1):
	file_write_hyp="./karan/T"+str(j)+"_hyp.txt"
	file_write_ref="./karan/T"+str(j)+"_ref.txt"
	file_hyp=open(file_write_hyp,"w")
	file_ref=open(file_write_ref,"w")
	file_opened_hyp[j]=file_hyp
	file_opened_ref[j]=file_ref
	

for i in range(1,participants+1):
	count_global=1
	for j in range(1,tasks+1):
		count_local=1
		ref_file_path="/home/seecat/Asr_gaze/dipti_hindi/reference/T"+str(j)
		ref_file=open(ref_file_path,"r")
		x=1
		for f in ref_file:
			lines[x]=f
			x=x+1
		for k in range(1,sentences+1):
			file_name="/home/seecat/integration/scripts/hindi_audio/P0"+str(i)+"_T"+str(j)+"_S"+str(k)+".txt"
			hypo_file=open(file_name,"r")
			best_hyp = hypo_file.readline().rstrip()
			if best_hyp == '':
				file_path_backup="/home/seecat/Asr_gaze/dipti_hindi/"
				file_name_backup="P01_T"+str(j)+"_S"+str(k)+".txt"
				file_read_backup=file_path_backup+file_name_backup
				hypo_file_backup=open(file_read_backup,"r")
				for f in hypo_file_backup:
					match_hypo=re.search('\"hypothesis\": "(.+)",',f)
					if match_hypo:
						best_hyp = match_hypo.group(1)
						break
				hypo_file_backup.close()
			hypo_file.close()
			best_hyp_local=best_hyp+" (P0"+str(i)+"_"+str(count_local)+")\n"
			best_hyp_global=best_hyp+" (P0"+str(i)+"_"+str(count_global)+")\n"
			ref_local=lines[k].rstrip()+" (P0"+str(i)+"_"+str(count_local)+")\n"
			ref_global=lines[k].rstrip()+" (P0"+str(i)+"_"+str(count_global)+")\n"
			file_opened_hyp[j].write(best_hyp_local)
			file_complete_hyp.write(best_hyp_global)
			file_opened_ref[j].write(ref_local)
			file_complete_ref.write(ref_global)
			count_local=count_local+1
			count_global=count_global+1
for j in range(1,tasks+1):
	file_opened_hyp[j].close()
	file_opened_ref[j].close()
	command1="/home/seecat/Asr_gaze/sclite -r ./karan/T"+str(j)+"_ref.txt -h ./karan/T"+str(j)+"_hyp.txt -i wsj"
	print commands.getstatusoutput(command1)[1]
command2="/home/seecat/Asr_gaze/sclite -r ./karan/complete_ref.txt -h ./karan/complete_hyp.txt -i wsj"
print commands.getstatusoutput(command2)[1]
file_complete_ref.close()
file_complete_hyp.close()
