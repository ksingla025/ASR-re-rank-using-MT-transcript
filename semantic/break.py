import sys,commands
for x in ["hin_wn"]:
        for w in range(49500):
                commands.getstatusoutput("head -1 "+x+" > hn_break/"+str(w+1))
                commands.getstatusoutput('sed -i "1d" '+x)
