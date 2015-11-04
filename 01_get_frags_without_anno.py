########################################
#command: python .py infile frag_1.bed frag_2.bed
########################################


import sys,os
infile=open(sys.argv[1],"r")
out1=open(sys.argv[2],"w")
out2=open(sys.argv[3],"w")
lines=infile.read().split('\n')
i=0
for line in lines:
    if len(line)>0:
        item=line.split('\t')
        out1.write(item[0]+'\t'+item[1]+'\t'+item[2]+'\t'+'pos'+str(i+1)+'\t'+'1'+'\t'+'.'+'\n')
        out2.write(item[3]+'\t'+item[4]+'\t'+item[5]+'\t'+'pos'+str(i+1)+'\t'+'1'+'\t'+'.'+'\n')
        i+=1
out1.close()
out2.close()
