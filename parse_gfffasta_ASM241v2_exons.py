import csv, os,sys
csv.field_size_limit(sys.maxsize)


input_data = list(csv.reader(open('/home/vdp5/data/gene_finder/ASM241v2_exongrab/ASM241v2_exons.fasta'),delimiter='\t'))

for index, data in enumerate(input_data):
	if data[0][0] == '>':
		print index