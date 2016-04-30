#extractFasta.py [allFasta] [outFasta] [subLst]

import sys,re

allFasta = open(sys.argv[1],'rU')
outFasta = open(sys.argv[2],'w')
subLst = open(sys.argv[3],'rU')

subSeq = []
for acc in subLst:
    subSeq.append(acc.rstrip())

for line in allFasta:
    seq = re.match(">(\S+)",line)
    if seq:
        name = seq.group(1)
        if name in subSeq:
            tag = 1
        else:
            tag = 0
    if tag:
        outFasta.write(line)
outFasta.close()
allFasta.close()
subLst.close()
