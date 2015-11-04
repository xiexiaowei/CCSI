########################################
#command: python .py infile
########################################


import sys,os
if os.path.exists("gen+reg.txt")==True:
    lines_1=open("frag_1.final","r").read().split('\n')
    lines_2=open("frag_2.final","r").read().split('\n')
    lines_3=open(sys.argv[1],"r").read().split('\n')
    out=open(sys.argv[1].split('.')[0]+".fin","w")
    for i in range(len(lines_1)):
	if len(lines_1[i])>0 and len(lines_2[i])>0 and len(lines_3[i])>0:
	    item_1=lines_1[i].split('\t')
	    item_2=lines_2[i].split('\t')
	    item_3=lines_3[i].split('\t')
            out.write(item_1[0]+'\t'+item_1[1]+'\t'+item_1[2]+'\t'+item_1[6]+'\t'+item_1[7]+'\t'+item_2[0]+'\t'+item_2[1]+'\t'+item_2[2]+'\t'+item_2[6]+'\t'+item_2[7]+'\t'+item_3[6]+'\t'+item_3[7]+'\t'+item_3[8]+'\n') 
    out.close()
	
	    
else:
    lines_1=open("frag_1.final","r").read().split('\n')
    lines_2=open("frag_2.final","r").read().split('\n')
    lines_3=open(sys.argv[1],"r").read().split('\n')
    out=open(sys.argv[1].split('.')[0]+".snp","w")
    for i in range(len(lines_1)):
        if len(lines_1[i])>0 and len(lines_2[i])>0 and len(lines_3[i])>0:
            item_1=lines_1[i].split('\t')
            item_2=lines_2[i].split('\t')
            item_3=lines_3[i].split('\t')
	    out.write(item_1[0]+'\t'+item_1[1]+'\t'+item_1[2]+'\t'+item_1[6]+'\t'+item_2[0]+'\t'+item_2[1]+'\t'+item_2[2]+'\t'+item_2[6]+'\t'+item_3[6]+'\t'+item_3[7]+'\t'+item_3[8]+'\n') 
    out.close()
