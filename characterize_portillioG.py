import matplotlib as mpl
mpl.use('Agg')


import csv, os, sys
import matplotlib.pyplot as plt
import seaborn as sns

input_data = list(csv.reader(open('/home/vdp5/data/gene_finder/ASM241v2_genes_exons/ASM214v2_genesexons.fasta'),delimiter='\t'))
portillo_g = zip(*list(csv.reader(open('/home/vdp5/data/other_data/portillo_Gfamily.txt'),delimiter='\t')))[0]

gene2numexon = {}

for index, data in enumerate(input_data):
	if data[0][0] != '>':
		continue
	for gene in portillo_g:
		if gene in data[0]:
			gene2numexon.setdefault(gene, []).append(1)

for gene in gene2numexon:
	gene2numexon[gene] = sum(gene2numexon[gene])

sns.distplot(gene2numexon.values(), kde=False, color='b')
plt.savefig('/home/vdp5/figures/portilloG_numberexons.pdf',bbox_inches='tight')
plt.close()
