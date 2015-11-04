########################################
#command: python .py
########################################


for i in range(1,3):
    infile=open("frag_"+str(i)+".txt","r")
    out=open("frag_"+str(i)+".step","w")
    lines=infile.read().split('\n')
    null_list=[]
    for line in lines:
        if len(line)>0:
            item=line.split('\t')
            if item[3] not in null_list:
                null_list.append(item[3])
                out.write('\n'+item[3]+'\t'+item[9])
            else:
                out.write(','+item[9])
    out.close()

for i in range(1,3):
    infile_1=open("frag_"+str(i)+".step","r")
    infile_2=open("frag_"+str(i)+".bed","r")
    out=open("frag_"+str(i)+".final","w")
    lines_1=infile_1.read().split('\n')
    lines_2=infile_2.read().split('\n')
    null_dir={}   #null_dir for snp
    for line in lines_1:
        if len(line)>0:
            item=line.split('\t')
            null_dir.keys().append(item[0])
            null_dir[item[0]]=item[1]
    for line in lines_2:
        if len(line)>0:
            item=line.split('\t')
            if item[3] in null_dir:
                out.write(line+'\t'+str(null_dir[item[3]])+'\n')
            else:
                out.write(line+'\t'+'null'+'\n')
    out.close()
