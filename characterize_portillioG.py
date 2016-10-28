# import matplotlib as mpl
# mpl.use('Agg')


import csv, os, sys
# import matplotlib.pyplot as plt
# import seaborn as sns

input_data = list(csv.reader(open('/home/vdp5/data/gene_finder/ASM241v2_genes_exons/ASM214v2_genesexons.fasta'),delimiter='\t'))
portillo_g = zip(*list(csv.reader(open('/home/vdp5/data/other_data/portillo_Gfamily.txt'),delimiter='\t')))[0]

portillodata = {}



gene2numexon = {}

for index, data in enumerate(input_data):
	if data[0][0] != '>':
		continue
	for gene in portillo_g:
		if gene in data[0]:
			gene2numexon.setdefault(gene, []).append(1)
			portillodata[data[0]] = input_data[index + 1][0]

gene3exons = []

for gene in gene2numexon:
	tot = sum(gene2numexon[gene])
	gene2numexon[gene] = sum(gene2numexon[gene])
	if tot == 3:
		gene3exons.append(gene)

print len(gene3exons)
# sns.countplot(gene2numexon.values(), color='b')
# plt.savefig('/home/vdp5/figures/portilloG_numberexons.pdf',bbox_inches='tight')
# plt.close()

output_data = open('/home/vdp5/data/gene_finder/ASM241v2_genes_exons/portillog_exons.fasta', 'w')

for line in sorted(portillodata.keys()):
	output_data.write('{}\n{}\n'.format(line, portillodata[line]))

output_data.close()



