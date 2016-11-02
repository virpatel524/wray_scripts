import csv
import os
import sys


input_dir = '/home/vdp5/data/cdna_analysis_ASM241_v2/vir_genes'
outputfle = open('/home/vdp5/data/gene_finder/ASM241v2_genes_exons/ASM214v2_genesexons.fasta', 'w')


for subdir, dirs, files in os.walk(input_dir):
	for alpha in files:
		tmp = list(csv.reader(open(os.path.join(input_dir, alpha)),delimiter='\t'))
