import os, sys, csv


data = list(csv.reader(open('/home/vdp5/data/vivax_2009/GCA_000002415.2_ASM241v2_genomic_edited_originalchromid.fasta'),delimiter='\t')) 

dnabank = ''

for index, alpha in enumerate(data):
	if alpha[0][0] == '>':
		continue
	else:
		newstr = alpha[0].upper()
		print newstr
