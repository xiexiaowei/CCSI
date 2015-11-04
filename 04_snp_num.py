########################################
#command: python .py infile
########################################


import sys,os
infile=open(sys.argv[1].split('.')[0]+".snp",'r')
out=open(sys.argv[1].split('.')[0]+".snp2",'w')
i=1
while i!=0:
    line=infile.readline()
    if len(line)>0:
        item=line.strip('\n').split('\t')
        snp1=item[3].split(',')
        snp2=item[7].split(',')
        if len(snp1)<500 and len(snp2)<500:
            out.write(line)
        elif len(snp1)<500 and len(snp2)>=500:
            out.write(item[0]+'\t'+item[1]+'\t'+item[2]+'\t'+item[3]+'\t'+item[4]+'\t'+item[5]+'\t'+item[6]+'\t'+'SNPnum>500'+'\t'+item[8]+'\t'+item[9]+'\t'+item[10]+'\n')
        elif len(snp1)>=500 and len(snp2)<500:
            out.write(item[0]+'\t'+item[1]+'\t'+item[2]+'\t'+'SNPnum>500'+'\t'+item[4]+'\t'+item[5]+'\t'+item[6]+'\t'+item[7]+'\t'+item[8]+'\t'+item[9]+'\t'+item[10]+'\n')
        else:
            out.write(item[0]+'\t'+item[1]+'\t'+item[2]+'\t'+'SNPnum>500'+'\t'+item[4]+'\t'+item[5]+'\t'+item[6]+'\t'+'SNPnum>500'+'\t'+item[8]+'\t'+item[9]+'\t'+item[10]+'\n')                
    else:
        i=0
out.close()
