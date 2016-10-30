import os
import csv

data = list(csv.reader(open('/home/vdp5/data/vivax_2009/GCA_000002415.2_ASM241v2_genomic_edited_originalchromid.fasta'),delimiter='\t'))

cur_chrome = 'beta'
chrom_dict = {}

for index, line in enumerate(data):
	if len(line) == 0:
		continue
	if line[0][0] == '>':
		cur_chrome = line[0]
	else:
		if cur_chrome not in chrom_dict:
			chrom_dict[cur_chrome] = line[0]
		else:
			chrom_dict[cur_chrome] = chrom_dict[cur_chrome] + line[0]


print chrom_dict


baes_new = '/home/vdp5/data/cdna_analysis_ASM241_v2/fasta_ASM241_v2'

for alpha in chrom_dict:
	newfle = open(baes_new + '/' + zeta + '.fasta', 'w')
	newfle.write('%s\n' %(alpha))
	newfle.write('%s\n'%(chrom_dict[alpha]))
