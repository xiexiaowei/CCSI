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
                out.write('...'+item[9])
    out.close()

for i in range(1,3):
    infile_1=open("frag_"+str(i)+".step","r")
    infile_2=open("frag_"+str(i)+".bed","r")
    out=open("frag_"+str(i)+".final","w")
    lines_1=infile_1.read().split('\n')
    lines_2=infile_2.read().split('\n')
    dir_0={};dir_1={} #dir_0 for id, dir_1 for name
    for line in lines_1:
        if len(line)>0:
            item=line.split('\t')
            dir_0.keys().append(item[0])
            dir_1.keys().append(item[0])
            gen_list=item[1].split('...')
            gen=gen_list[0].split('*')
            dir_0[item[0]]=gen[0]
            dir_1[item[0]]=gen[1]
            for j in range(1,len(gen_list)):
                gen=gen_list[j].split('*')
                dir_0[item[0]]+=','+gen[0]
                dir_1[item[0]]+=','+gen[1]    
    for line in lines_2:
        if len(line)>0:
            item=line.split('\t')
            if item[3] in dir_0 and item[3] in dir_1:
                out.write(line+'\t'+str(dir_0[item[3]])+'\t'+str(dir_1[item[3]])+'\n')
            elif item[3] in dir_0 and item[3] not in dir_1:
                out.write(line+'\t'+str(dir_0[item[3]])+'\t'+'null'+'\n')     
            elif item[3] not in dir_0 and item[3] in dir_1:
                out.write(line+'\t'+'null'+'\t'+str(dir_1[item[3]])+'\n')
            else:
                out.write(line+'\t'+'null'+'\t'+'null'+'\n')
    out.close()
