from Bio.Data import CodonTable
from Bio.Seq import translate
table = CodonTable.ambiguous_dna_by_id[1]


import csv, os, sys
# import matplotlib.pyplot as plt
# import seaborn as sns

input_data = list(csv.reader(open('/home/vdp5/data/gene_finder/ASM241v2_genes_exons/ASM214v2_genesexons.fasta'),delimiter='\t'))
print input_data
portillo_g = zip(*list(csv.reader(open('/home/vdp5/data/other_data/portillo_Gfamily.txt'),delimiter='\t')))[0]

portillodata = {}



gene2numexon = {}

for index, data in enumerate(input_data):
	print data
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



exon1fle = open('/home/vdp5/data/gene_finder/ASM241v2_genes_exons/gfamily_exon1.fasta','w')
exon2fle = open('/home/vdp5/data/gene_finder/ASM241v2_genes_exons/gfamily_exon2.fasta','w')
exon3fle = open('/home/vdp5/data/gene_finder/ASM241v2_genes_exons/gfamily_exon3.fasta','w')



for name in sorted(portillodata):
	for alpha in gene3exons:
		if alpha in name:
			if 'exon1' in name:
				exon1fle.write(name + '\n')
				exon1fle.write(translate(portillodata[name]) + '\n')
			if 'exon2' in name:
				exon2fle.write(name + '\n')
				exon2fle.write(translate(portillodata[name]) + '\n')
			if 'exon3' in name:
				exon3fle.write(name + '\n')
				exon3fle.write(translate(portillodata[name]) + '\n')

# sns.countplot(gene2numexon.values(), color='b')
# plt.savefig('/home/vdp5/figures/portilloG_numberexons.pdf',bbox_inches='tight')
# plt.close()

output_data = open('/home/vdp5/data/gene_finder/ASM241v2_genes_exons/portillog_exons.fasta', 'w')


for line in sorted(portillodata.keys()):
	output_data.write('{}\n{}\n'.format(line, portillodata[line]))

output_data.close()



