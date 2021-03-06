import os
import csv

exitfle = open('/home/vdp5/data/cdna_analysis_SAMEA2376790/gene2exon_PV01.txt', 'w')
rootdir = '/home/vdp5/data/cdna_analysis_SAMEA2376790/vir_genes'
flag_file = open('/home/vdp5/data/cdna_analysis_SAMEA2376790/flagged_genes.txt', 'w')

gene2exons = {}

for subdir, dirs, files in os.walk(rootdir):
	sortedfles = sorted(files)
	if len(sortedfles)!=2:
		continue
	tmp = list(csv.reader(open(os.path.join(subdir, sortedfles[0])),delimiter='\t'))
	gene='_'.join(sortedfles[0].split('_')[:2])
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


exitfle.close()
flag_file.close()