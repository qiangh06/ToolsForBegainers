#count mapping depth for Reseuqencing mapping

import os, sys, glob, re
inFiles = glob.glob(sys.argv[1]+"/*.realn.bam")
i=0;
for _file in inFiles:
    fileName = os.path.split(_file)[1].split(".")[0]
    cmd = "bamtools stats -in %s > %s.stat"%(_file,fileName)
    os.system(cmd)
    i = i+1
    print i

statOut = open("allStat",'w')
firstLine = "AccName,Total reads,Mapped reads,Mapped rate\n"
statOut.write(firstLine)
allFiles = glob.glob("./*.stat")
print "Combine..."
for _file in allFiles:
    name1 = os.path.split(_file)[1].split(".")[0]
    content = open(_file,'rU')
    for line in content:
        line = line.rstrip()
        if re.search(r'^Total',line):
            col1 = line.split(" ")[-1]
        elif re.search(r'^Mapped',line):
            col2 = line.split(" ")[-1].split("\t")[0]
            col3 = line.split(" ")[-1].split("\t")[1]
            col3 = col3.replace("(","")
            col3 = col3.replace("%)","")
    content.close()
    _line = name1+","+col1+","+col2+","+col3+"\n"
    statOut.write(_line)
print "Done!"
statOut.close()
