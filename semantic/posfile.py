import sys,commands,re
f=open(sys.argv[1],"r").readlines()#lattice file
w=open(sys.argv[2],"w")#temp file
w.write("<s>\n")
for x in range(len(f)):
	line=f[x]
	spl=line.split()
	if len(spl)<=1:
		if x==len(f)-1:
			w.write("</s>")
		else:
			w.write("</s>\n<s>\n")
	else:
		w.write(spl[2]+"\n")
#print "/home/seecat/experiments/speech/phone_dict_hin/scripts/hindi-pos-tagger-2.0/bin/tnt -H -v0 /home/seecat/experiments/speech/phone_dict_hin/scripts/hindi-pos-tagger-2.0/models/hindi "+sys.argv[2]+" |  sed -e 's/\\t\+/\\t/g' | /home/seecat/experiments/speech/phone_dict_hin/scripts/hindi-pos-tagger-2.0/bin/lemmatiser.py /home/seecat/experiments/speech/phone_dict_hin/scripts/hindi-pos-tagger-2.0/models/hindi.lemma > hindi.sample.out.txt"
#print commands.getstatusoutput("/home/seecat/experiments/speech/phone_dict_hin/scripts/hindi-pos-tagger-2.0/bin/tnt -H -v0 /home/seecat/experiments/speech/phone_dict_hin/scripts/hindi-pos-tagger-2.0/models/hindi "+sys.argv[2]+" |  sed -e 's/\\t\+/\\t/g' | /home/seecat/experiments/speech/phone_dict_hin/scripts/hindi-pos-tagger-2.0/bin/lemmatiser.py /home/seecat/experiments/speech/phone_dict_hin/scripts/hindi-pos-tagger-2.0/models/hindi.lemma > hindi.sample.out.txt")
w.close()
print commands.getstatusoutput("/home/seecat/experiments/speech/phone_dict_hin/scripts/hindi-pos-tagger-2.0/bin/tnt -H -v0 /home/seecat/experiments/speech/phone_dict_hin/scripts/hindi-pos-tagger-2.0/models/hindi "+ sys.argv[2]+" |  sed -e 's/\t\+/\t/g' | /home/seecat/experiments/speech/phone_dict_hin/scripts/hindi-pos-tagger-2.0/bin/lemmatiser.py /home/seecat/experiments/speech/phone_dict_hin/scripts/hindi-pos-tagger-2.0/models/hindi.lemma >hindi.sample.out.txt")
