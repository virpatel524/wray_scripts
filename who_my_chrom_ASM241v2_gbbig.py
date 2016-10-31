import os, csv, sys

import Bio
from Bio.Seq import Seq


data = list(csv.reader(open('/home/vdp5/data/gene_finder/vir_all_ASM241v2/allgenes.txt'),delimiter='\t'))

data = [a[0] for a in data]
gene2seq = {}
for index, alpah in enumerate(data):
	if index % 2 != 0:
		continue
	else:
		gene2seq[alpah[1:]] = data[index + 1]


gene2chromfle = open('/home/vdp5/data/gene_finder/ASM241v2_genes_exons/gene2chrom.txt','w')

os.chdir('/home/vdp5/data/cdna_analysis_ASM241_v2/fasta_ASM241_v2')
for gene in gene2seq:
	bash_process = 'grep -i -r -l '
