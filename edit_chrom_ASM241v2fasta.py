import csv, os

input_data = list(csv.reader(open('/home/vdp5/data/vivax_2009/GCA_000002415.2_ASM241v2_genomic_originalchromid.fasta','r'),delimiter='\t'))
output_data = open('/home/vdp5/data/vivax_2009/GCA_000002415.2_ASM241v2_genomic_edited_originalchromid.fasta','w')


for alpha in input_data:
	if alpha[0][0] == '>':
		print alpha[0].split(' ')[0]


output_data.close()