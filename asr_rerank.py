#!/usr/bin/python

import sys
import re
import os
import commands

name = sys.argv[1]    
name2 = sys.argv[2]
name3 = sys.argv[3]
#name4 = sys.argv[4]

print "getting machine translation"
name_txt=re.sub(".wav",".txt",os.path.basename(name))

##################### " It will be the Transcript now " ###########################

print commands.getstatusoutput("/srv/tools/mosesdecoder/bin/moses -f /home/seecat/MT/experiments/hin-eng/working_dir/moses.tuned.ini.1 -n-best-list /home/seecat/integration/data/MT/translation/"+name_txt+" "+name3+" < /home/seecat/integration/data/MT/english_hindi_experiment/"+name_txt)
#iame_txt=re.sub(".wav",".txt",os.path.basename(name))<F5>


#print "/srv/tools/mosesdecoder/bin/moses -f /home/seecat/MT/anu/experiments/baseline_180k/working_dir/moses.tuned.ini.1 -n-best-list /home/seecat/integration/data/MT/translation/"+name_txt+" "+name3+" < /home/seecat/integration/data/MT/eng_ref/"+name_txt

print "machine translation hypothesis created"
print commands.getstatusoutput("python mt_lattice.py /home/seecat/integration/data/MT/translation/"+name_txt+" /home/seecat/integration/data/MT/artificial/"+name_txt+" 1")

print "python mt_lattice.py /home/seecat/integration/scripts/English_Junaid/synmt/"+name_txt+" /home/seecat/integration/data/MT/simple/"+name_txt+" "+name3

#print "python mt_lattice.py /home/seecat/integration/MT/translation/"+name_txt+" /home/seecat/integration/MT/"+name_txt+" "+name3

#commands.getstatusoutput("/srv/tools/mosesdecoder/bin/moses -f /home/seecat/MT/experiments/baseline180k/working-dir/moses.tuned.1.ini -n-best-list /home/seecat/integration/data/MT/translated/"+name_txt+" "+name3+" < /home/seecat/integration/data/MT/eng_ref/"+name_txt)

print "getting connection to watson"
commands.getstatusoutput("curl --data-binary @"+name+" http://wmssp.research.att.com/seecat/asr --header 'accept: application/prettyjson' --header 'content-type: audio/wav' --header 'trace: verbose' > oo")
print "----------------------------------\n"
    

print "creating lattices\n"
print commands.getstatusoutput("python /home/seecat/integration/scripts/asr_lattice_new.py oo /home/seecat/integration/data/speech/asr_lattices/asr_lattice.txt English_arvind/asr/"+name_txt)
print "python /home/seecat/integration/scripts/asr_lattice_new.py oo /home/seecat/integration/data/speech/asr_lattices/asr_lattice.txt dump/"+name_txt

print "-----audio file lattice created-----\n"

#print name_txt
    
print "------making EDIT fst text input ready----"
print commands.getstatusoutput("python edit_fst_input.py /home/seecat/integration/data/MT/artificial/"+name_txt+" /home/seecat/integration/data/speech/asr_lattices/asr_lattice.txt")
    

print "----creating input file for lattices----\n"
print commands.getstatusoutput("python fst_inp_symbol.py /home/seecat/integration/data/speech/asr_lattices/asr_lattice.txt /home/seecat/integration/data/MT/artificial/"+name_txt+"  /home/seecat/integration/data/inputsym.txt")
print "------lattice input symbols files created----\n"
    

print "\n\n"
print "fstcompile --isymbols=/home/seecat/integration/data/inputsym.txt --osymbols=/home/seecat/integration/data/inputsym.txt /home/seecat/integration/data/speech/asr_lattices/asr_lattice.txt > /home/seecat/integration/data/sp.fst"

print commands.getstatusoutput("fstcompile --isymbols=/home/seecat/integration/data/inputsym.txt --osymbols=/home/seecat/integration/data/inputsym.txt /home/seecat/integration/data/speech/asr_lattices/asr_lattice.txt > /home/seecat/integration/data/sp.fst")


print commands.getstatusoutput("fstcompile --isymbols=/home/seecat/integration/data/inputsym.txt --osymbols=/home/seecat/integration/data/inputsym.txt /home/seecat/integration/data/MT/artificial/"+name_txt+" > /home/seecat/integration/data/mt.fst")

print "---------MT fst created-------\n"

print "fstcompile --isymbols=/home/seecat/integration/data/inputsym.txt --osymbols=/home/seecat/integration/data/inputsym.txt /home/seecat/integration/data/edit > /home/seecat/integration/data/edit.fst"
    
print commands.getstatusoutput("fstcompile --isymbols=/home/seecat/integration/data/inputsym.txt --osymbols=/home/seecat/integration/data/inputsym.txt /home/seecat/integration/data/edit > /home/seecat/integration/data/edit.fst")             
print "---------EDIT fst created-----\n"

print commands.getstatusoutput("fstarcsort --sort_type=ilabel /home/seecat/integration/data/edit.fst edit1.fst") 
print commands.getstatusoutput("fstcompose /home/seecat/integration/data/sp.fst edit1.fst > temp.fst") 
print commands.getstatusoutput("fstarcsort --sort_type=olabel temp.fst > temp1.fst")
print commands.getstatusoutput("fstcompose temp1.fst /home/seecat/integration/data/mt.fst > /home/seecat/integration/data/composed.fst")    
print "-----------composes fst built------"

commands.getstatusoutput("fstshortestpath /home/seecat/integration/data/composed.fst |fstproject --project_output=false | fstrmepsilon | fstprint --isymbols=/home/seecat/integration/data/inputsym.txt > hi")
#commands.getstatusoutput("fstshortestpath /home/seecat/integration/data/composed.fst | fstprint --isymbols=/home/seecat/integration/data/inputsym.txt > hi")
commands.getstatusoutput("python /home/seecat/integration/scripts/short_hyp_2_str.py "+name2)

#commands.getstatusoutput(
#    commands.getstatusoutput("rm /home/seecat/integration/data/speech/temp/*")
