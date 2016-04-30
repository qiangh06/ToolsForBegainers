#convert the sequence file, usually snp data, to fasta file.
#input format: first column is seq name followed by SNPs
import sys
inF = open(sys.argv[1],'rU')
out = open(sys.argv[2],'w')
for i in inF:
    _line = i.rstrip().split("\t")
    head = ">"+_line[0]+"\n"
    seq = "".join(_line[1:])+"\n"
    out.write(head+seq)
out.close()
inF.close()
