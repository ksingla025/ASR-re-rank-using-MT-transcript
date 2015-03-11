#to replace words from string with synset ID
import sys,commands,codecs,re
f=open(sys.argv[1]).readline().decode("utf-8","replace")# file containing gold string
w=codecs.open(sys.argv[2],"w","utf-8")
w.write("<s>\n")
w.write("\n".join(f.split()))
#print "\n".join(f.split())
w.write("\n</s>")
w.close()
print commands.getstatusoutput("/home/seecat/experiments/speech/phone_dict_hin/scripts/hindi-pos-tagger-2.0/bin/tnt -H -v0 /home/seecat/experiments/speech/phone_dict_hin/scripts/hindi-pos-tagger-2.0/models/hindi "+ sys.argv[2]+" |  sed -e 's/\t\+/\t/g' | /home/seecat/experiments/speech/phone_dict_hin/scripts/hindi-pos-tagger-2.0/bin/lemmatiser.py /home/seecat/experiments/speech/phone_dict_hin/scripts/hindi-pos-tagger-2.0/models/hindi.lemma >hindi.gold.out.txt")
print commands.getstatusoutput("python /home/seecat/integration/scripts/aniruddha/demo.py hindi.gold.out.txt gold_temp /home/seecat/integration/scripts/aniruddha/merge_mapping_dic/"+re.sub(".txt","_merge.txt",sys.argv[1]))
f=open("gold_temp","r").read().split()
f.remove("<s>")
f.remove("</s>")
f=" ".join(f)
w=open(sys.argv[2],"w")
w.write(f+"\n")
