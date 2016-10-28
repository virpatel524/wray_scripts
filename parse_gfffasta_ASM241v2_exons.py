import csv, os,sys
import operator
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
		gene2exon.setdefault(gene, []).append([ident, input_data[index + 1][0]])

for gene in gene2exon:
	newlst = sorted(gene2exon[gene], key=lambda x: x[0])
	counter = 1
	for alpha in newlst:
		output_data.write('>{}_exon{}\n'.format(gene, counter))
		output_data.write('{}\n'.format(alpha[-1]))
		counter += 1


		

output_data.close()

