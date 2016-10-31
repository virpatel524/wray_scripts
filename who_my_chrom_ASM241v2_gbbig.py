import os, csv, sys

data = list(csv.reader(open('/home/vdp5/data/gene_finder/vir_all_ASM241v2/allgenes.txt'),delimiter='\t'))


chrom2seq = {}

for index, alpah in data:
	if index % 2 != 0:
		continue
	else:
		chrom2seq[alpah[0]] = data[index][0]

print chrom2seq