import csv, os, sys

input_data = list(csv.reader(open('/home/vdp5/data/gene_finder/ASM241v2_genes_exons/ASM214v2_genesexons.fasta'),delimiter='\t'))
portillo_g = zip(*list(csv.reader(open('/home/vdp5/data/other_data/portillo_Gfamily.txt'),delimiter='\t')))[0]

print portillo_g