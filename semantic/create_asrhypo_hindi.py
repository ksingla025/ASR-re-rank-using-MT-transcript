#!/usr/bin/python

import sys
import re
import os
import commands
## Hitting watson for english audio files of tourism domain
## usage: ./create_asr_hypothesis.py <path of the folder containing the audio files>

cmd1 = "ls "+sys.argv[1]+"/*.hyp > temp.txt"
os.system(cmd1)
f_name = open("temp.txt", "r")
out_num = open(sys.argv[3],'w')
output = open(sys.argv[4],'w')
#numbers = 0
for line in f_name:
	line1=line.rstrip()
	line2="\\ ".join(line1.split())
	print "this is line2 === "+line2	
	line3=line2.split(".")
#	command = "curl --data-binary @"+ line2 +" http://wmssp.research.att.com/seecat.hi/asr --header 'accept: application/prettyjson' --header 'content-type: audio/wav' --header 'trace: verbose' | grep \\\"hypothesis\\\"|cut -f2 -d':'|tee n-best > oo"
	g = line3[0]+'.txt'
	print "this is g ====="+g
#	file1 = open('oo','r')
#	gg = open(sys.argv[2]+g,'w')
	d = g.split('/')
	print d[1]
	gg = sys.argv[2]+'/'+d[1]
	print "this is gg ======"+gg
	

	file1 = open(line2,'r')
#	print g
#	print "=========================================="+str(line2)+"======================================"
	counter = 0
	maxi = 0
	out = ''
	
	counterss = 0
	for line1 in file1:
		print line1
		counter = counter + 1
		flag = 0
		temp = open("tempo"+str(counter),'w')
#		count = count + 1
        	line1 = line1
#n		print "============================="+line1+"==============================="
        	temp.write(line1)
		temp.write('\n')
		temp.close()
#		print "=========this is ref ====="+d[1]+"==============="
		commands.getstatusoutput("/home/seecat/Asr_gaze/sclite -r "+gg+" -h tempo"+str(counter)+" -i wsj > hi")
#		print "/home/seecat/Asr_gaze/sclite -r hindi_ref/"+d[1]+" -h tempo"+str(counter)+" -i wsj > hi"
		new = open("hi",'r')
		count = 0
		for x in new:
#			print x
			count = count + 1
#			print "=========="+str(count)+"========"
			temp2 = 1.0
#			print line1 + " -----score is === : " + str(tess)
			
			if count == 15:
#				print x
				temp1 = x.split()
				temp2 = temp1[5]
				temp3 = line1.rstrip()
				print line1 + " -----score is === : " + str(temp2)
#				print temp2
			if float(temp2) > float(maxi):
				maxi = temp2
				number = counter
				out = line1
#				flag = 1
#				break
#				print 
#				print out
	
#		if flag == 1:
#			break
#		print ('\n\n')
		counterss = counterss + 1
#		commands.getstatusoutput("mv hi temp"+str(counterss))
	commands.getstatusoutput("rm tempo*")		

#	numbers = numbers+1	
	out_num.write(str(out.rstrip())+"  ----max score is === "+str(maxi))
#	print maxi
	output.write(out)
#	output.write('\n')
	
#	os.system(command)
	commands.getstatusoutput("rm temp.txt")
	

