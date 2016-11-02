import os, sys, csv


data = list(csv.reader(open('/home/vdp5/data/vivax_2009/GCA_000002415.2_ASM241v2_genomic_edited_originalchromid.fasta'),delimiter='\t')) 
ouputfle = open('/home/vdp5/data/cdna_analysis_ASM241_v2/fasta_full_exon_determine.fasta', 'w')
dnabank = ''

for index, alpha in enumerate(data):
	if alpha[0][0] == '>':
		continue
	else:
		newstr = alpha[0].upper()
		dnabank += newstr

ouputfle.write('>fullthing\n')
ouputfle.write(dnabank + '\n')

ouputfle.close()