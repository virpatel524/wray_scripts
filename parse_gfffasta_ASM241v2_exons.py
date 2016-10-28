import csv, os,sys
csv.field_size_limit(sys.maxsize)


input_data = list(csv.reader(open('/home/vdp5/data/gene_finder/ASM241v2_exongrab/ASM241v2_exons.fasta'),delimiter='\t'))
output_data = open('/home/vdp5/data/gene_finder/ASM241v2_genes_exons/' + 'ASM214v2_genesexons.fasta', 'w')
gene2exon = {}

for index, data in enumerate(input_data):
	if data[0][0] != '>':
		continue
	tmp = data[0].split(';')
	tmp[0] = tmp[0][1:]
	if tmp[0] == 'exon':
		ident = tmp[1][5:]
		gene = tmp[4].split(' ')[-1][:-1]
		gene2exon.setdefault(gene, []).append([ident, input_data[index + 1]])



