########################################
#1. read config
#2. annotation of gene or gene+regulatory_region
#3-1. annotation with snp
#3-2. annotation without snp
#command: python run.py -i1 infile -i2 genome -i3 regulatory_region -i4 snp -o
#example1: python run.py -i1 3c-1.step -i2 fission.tss -i3 no -i4 no -o
#example2: python run.py -i1 hic-39.step -i2 mm10.tss -i3 no -i4 mm10.snp -o
########################################


import sys,os
infile=sys.argv[2]
genome=sys.argv[4]
regulatory_region=sys.argv[6]
snp=sys.argv[8]
print 'read config done'



########################################
#This was intended for annotating TSS and regulatory regions in chromatin fragments.
########################################
if regulatory_region!='no':
    pass
else:
    os.system('touch null_file')
    regulatory_region="null_file"
    
os.system('python 01_get_frags_without_anno.py '+infile+' frag_1.bed frag_2.bed') #get frag_1 and frag_2
os.system('cat '+genome+' '+regulatory_region+' > gen+reg.txt') #genome + regulatory_region
os.system('intersectBed -a frag_1.bed -b gen+reg.txt -wb > frag_1.txt') #annotation of tss and regul
os.system('intersectBed -a frag_2.bed -b gen+reg.txt -wb > frag_2.txt') #annotation of tss and regul
os.system('python 02_stat_tss,regul_in_frags.py') #stat id and name of TSS/enhancer separately in frag_1,2
os.system('python 03_merge_frags_with_anno.py '+infile) #merge frag_1,2 with annotation
os.remove('frag_1.bed')
os.remove('frag_2.bed')
os.remove('gen+reg.txt')
os.remove('frag_1.txt')
os.remove('frag_2.txt')
os.remove('frag_1.step')
os.remove('frag_2.step')
os.remove('frag_1.final')
os.remove('frag_2.final')
if os.path.exists("null_file")==True:
    os.remove('null_file')
else:
    pass
print 'annotation with gene and regulatory region done'
##only remain .fin file for next





########################################
#This was designed for annotating SNP in chromatin fragments.
########################################
if snp!='no':
    os.system('python 01_get_frags_without_anno.py '+infile+' frag_1.bed frag_2.bed') #get frag_1 and frag_2
    os.system('intersectBed -a frag_1.bed -b '+snp+' -wb > frag_1.txt') #annotation of snp
    os.system('intersectBed -a frag_2.bed -b '+snp+' -wb > frag_2.txt') #annotation of snp
    os.system('python 02_stat_snp_in_frags.py') #stat SNP in frag_1,2
    os.system('python 03_merge_frags_with_anno.py '+infile) #merge frag_1,2 with annotation
    os.system('python 04_snp_num.py '+infile) #--SNPnum>500
    os.system('python 05_merge_tss,regul_and_snp.py '+infile) #--merge .fin and .snp2
    os.remove('frag_1.bed')
    os.remove('frag_2.bed')
    os.remove('frag_1.txt')
    os.remove('frag_2.txt')
    os.remove('frag_1.step')
    os.remove('frag_2.step')
    os.remove('frag_1.final')
    os.remove('frag_2.final')
    os.remove(sys.argv[2].split('.')[0]+".snp")
    os.remove(sys.argv[2].split('.')[0]+".snp2")
    os.remove(sys.argv[2].split('.')[0]+".fin")
    print 'annotation with snp done'  
    
        
else:
    os.system('python 05_merge_tss,regul_and_snp.py '+infile) #--merge .fin and .snp2
    os.remove(sys.argv[2].split('.')[0]+".fin")
    print 'annotation without snp done'   

    
