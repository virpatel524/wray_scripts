import csv
import os
import sys


input_dir = '/home/vdp5/data/cdna_analysis_ASM241_v2/vir_genes'
outputfle = open('/home/vdp5/data/gene_finder/ASM241v2_genes_exons/ASM214v2_genesexons.fasta', 'w')


for subdir, dirs, files in os.walk(input_dir):
	for splignout in files:
		tmp = list(csv.reader(open(os.path.join(input_dir, splignout)),delimiter='\t'))
		gene='_'.join(splignout.split('_')[:2])
		exonnums = []
		tmplst = []
		for alpha in tmp:
			if len(alpha) == 0: continue
			if 'Exon' in alpha[0]:
				data = alpha[0].split(' ')
				if float(data[-1]) < 0.95:
					continue 
				tmplst.append('exon{}:{}'.format(data[2], data[3].split('(')[-1].split(',')[0]))

				exonnums.append(int(data[2]))
		tmplst = sorted(tmplst)
		if len(tmplst) != len(list(set(exonnums))):
			flag_file.write('{}\n'.format(gene))
			continue
		exitfle.write('>{}\n'.format(gene))
		exitfle.write('{}\n'.format('\n'.join(tmplst)))


