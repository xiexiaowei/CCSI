README

##########################################################################################
Analysis pipeline is a software package, which contains seven scripts as follows: 
(1)01_get_frags_without_anno.py 
(2)02_stat_snp_in_frags.py
(3)02_stat_tss,regul_in_frags.py
(4)03_merge_frags_with_anno.py         
(5)04_snp_num.py
(6)05_merge_tss,regul_and_snp.py
(7)run.py (main script)

##########################################################################################
Anyone can use the analysis pipeline free of charge for non-commercial use. 
Please send bug reports to: xiexw3@mail2.sysu.edu.cn 
This README file covers the following topics:

1. Prerequest for analysis pipeline
2. Prepare input files
3. How to run
4. output files explanation

##########################################################################################
1. Prerequest for analysis pipeline
Before running, users need to check whether Python and bedtools have been installed in the Linux machine. 

##########################################################################################
2.Prepare input files
Now let us see the contents of four input files.

1). "infile" contains pairwise interactional fragments, contact, FDR and p-value.
"contact" is the raw read counts of two interactional fragments. A few references didn't release this item, and we adopt "NA" to replace it.
FDR and p-value are provided for two interactional fragments. (Each of which could be NA for the missing value.)
The format: chr	start1	end1	chr	start2	end2	contact	FDR	p-value 
A example:
chr1	1098891	1133667	chr1	1007040	1021821	60	NA	2.68592821617844e-07
chr1	1065326	1112869	chr1	1112870	1127281	85	NA	1.55529269942366e-09

2). "genome" describes the transcription start sites(TSSs) of genes, which is used for locating promoters in interactional fragments.
The format: chr TSS TSS+1 Ensembl_id*gene_name score strand
A example:
chr1	11869	11870	ENSG00000223972*DDX11L1	1	+
chr1	29570	29571	ENSG00000227232*WASH7P	1	-

3). "regulatory_region" presents the position information of regulatory region like enhancer.
The forma: chr enhancer_midpoint enhancer_midpoint+1 enhancer_id*enhancer_name score strand
A example:
chr1	905707	905708	enhancer1*enhancer1	1	.
chr1	911207	911208	enhancer2*enhancer2	1	.

4). "snp" presents the position information of SNP.
The format: chr start end SNPname score strand
A example:
chr1	10019	10020	rs376643643	1	+
chr1	10056	10056	rs373328635	1	+

##########################################################################################
3.How to run analysis pipeline?
description: Analysis pipeline is used for annotating interactional fragments with genes, regulatory regions and SNPs in them,
This contributes to discerning which genome elements interact in space and facilitates exploring transcriptional regulatory mechanism in disease pathogenesis associated with spatial interaction among genes, enhancers and SNPs.

Usage: python run.py -i1 infile -i2 genome -i3 regulatory_region -i4 snp -o
-i1: input file1---infile
-i2: input file2---genome
-i3: input file3---regulatory_region
-i4: input file4---snp
-o: output file, which will be named according to infile.

Example use 1: python run.py -i1 3c-1.step -i2 fission.tss -i3 no -i4 no -o
Example use 2: python run.py -i1 hic-39.step -i2 mm10.tss -i3 no -i4 mm10.snp -o
Example use 3: python run.py -i1 hic-22.step -i2 hg38.tss -i3 IMR90.hg38.enhancer -i4 hg38.snp -o

Note: As for regulatory_region and snp, if corresponding files do not exist for certain cell line, you can make them equal to "no" like above:

##########################################################################################
4. output files explanation
The output will have 15 items: chr	start1	end1	ID1	name1	snp1	chr	start2	end2	ID2	name2	snp2	contact	FDR	p-value
chr	start1	end1: fragment1
ID1: all gene Ensembl IDs in fragment1
name1: all gene names in fragment1
snp1: all SNPs in fragment1
chr	start2	end2: fragment2
ID2: similar to ID1
name2: similar to name1
snp2: similar to snp1
contact: as above
FDR: as above
p-value: as above
Note: Fragment1 and fragment2 are spatially interacted. As for the fragments having no items, we assign "null" to them.

Example 1 output: (.xls format)
chr	start1	end1	ID1	name1	snp1	chr	start2	end2	ID2	name2	snp2	contact	FDR	p-value
chr1	1098891	1133667	ENSG00000131591,enhancer18	C1orf159,enhancer18	SNPnum>500	chr1	1007040	1021821	ENSG00000231702,ENSG00000224969,enhancer10,ENSG00000188157	RP11-54O7.10,RP11-54O7.11,enhancer10,AGRN	rs188031529,rs114829796…	60	NA	2.69E-07
chr1	1065326	1112869	ENSG00000237330,enhancer16,enhancer17	RNF223,enhancer16,enhancer17	SNPnum>500	chr1	1112870	1127281	ENSG00000131591,enhancer18	C1orf159,enhancer18	rs183985652,rs142315333…	85	NA	1.56E-09





