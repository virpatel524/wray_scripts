import os, sys, csv


data = list(csv.reader(open('/home/vdp5/data/vivax_2009/GCA_000002415.2_ASM241v2_genomic_edited_originalchromid.fasta'),delimiter='\t')) 

dnabank = ''

for index, alpha in enumerate(data):
	if index % 2 == 0:
		continue
	else:
		print alpha
