import sys,commands
for x in ["eng_data"]:
	for w in range(200):
		commands.getstatusoutput("head -1 "+x+" > P01_T1_S"+str(w+1)+".txt")
		commands.getstatusoutput('sed -i "1d" '+x)
