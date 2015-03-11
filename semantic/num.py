import sys

f = open(sys.argv[1],'r')
g = open(sys.argv[2],'w')
counter = 0
for line in f:
	counter = counter + 1
	line1 = line.rstrip()
        line1 = line1.replace("\n","")+" (P01_"+str(counter)+")"
        g.write(line1)
	g.write('\n')

