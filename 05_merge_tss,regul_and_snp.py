########################################
#command: python .py infile
########################################


import sys,os   
if os.path.exists(sys.argv[1].split('.')[0]+".snp2")==True:
    infile1=open(sys.argv[1].split('.')[0]+".fin","r")
    infile2=open(sys.argv[1].split('.')[0]+".snp2","r")
    out=open(sys.argv[1].split('.')[0]+".xls","w")
    out.write('chr'+'\t'+'start1'+'\t'+'end1'+'\t'+'ID1'+'\t'+'name1'+'\t'+'snp1'+'\t'+'chr'+'\t'+'start2'+'\t'+'end2'+'\t'+'ID2'+'\t'+'name2'+'\t'+'snp2'+'\t'+'contact'+'\t'+'FDR'+'\t'+'p-value'+'\n')    
    i=1
    while i!=0:
        line_1=infile1.readline()
        line_2=infile2.readline()
        if len(line_1)>0 and len(line_2)>0:
            item_1=line_1.strip('\n').split('\t')
            item_2=line_2.strip('\n').split('\t')
            out.write(item_1[0]+'\t'+item_1[1]+'\t'+item_1[2]+'\t'+item_1[3]+'\t'+item_1[4]+'\t'+item_2[3]+'\t'+item_1[5]+'\t'+item_1[6]+'\t'+item_1[7]+'\t'+item_1[8]+'\t'+item_1[9]+'\t'+item_2[7]+'\t'+item_1[10]+'\t'+item_1[11]+'\t'+item_1[12]+'\n')
        else:
            i=0
    out.close()

else:
    infile=open(sys.argv[1].split('.')[0]+".fin","r")
    out=open(sys.argv[1].split('.')[0]+".xls","w")
    out.write('chr'+'\t'+'start1'+'\t'+'end1'+'\t'+'ID1'+'\t'+'name1'+'\t'+'snp1'+'\t'+'chr'+'\t'+'start2'+'\t'+'end2'+'\t'+'ID2'+'\t'+'name2'+'\t'+'snp2'+'\t'+'contact'+'\t'+'FDR'+'\t'+'p-value'+'\n')    
    lines=infile.read().split('\n')   
    for line in lines:
        if len(line)>0:
            item=line.split('\t')    
            out.write(item[0]+'\t'+item[1]+'\t'+item[2]+'\t'+item[3]+'\t'+item[4]+'\t'+'null'+'\t'+item[5]+'\t'+item[6]+'\t'+item[7]+'\t'+item[8]+'\t'+item[9]+'\t'+'null'+'\t'+item[10]+'\t'+item[11]+'\t'+item_1[12]+'\n')
    out.close()     
    
