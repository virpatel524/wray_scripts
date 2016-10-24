import os
import csv

exitfle = open('/home/vdp5/data/cdna_analysis_SAMEA2376790/gene2exon_PV01.txt', 'w')
rootdir = '/home/vdp5/data/cdna_analysis_SAMEA2376790/vir_genes'


gene2exons = {}

for subdir, dirs, files in os.walk(rootdir):
	sortedfles = sorted(files)
	if len(sortedfles)!=2:
		continue
	tmp = list(csv.reader(open(os.path.join(subdir, sortedfles[0])),delimiter='\t'))
	gene=sortedfles[0].split('_')[1]
	tmplst = []
	for alpha in tmp:
		if len(alpha) == 0: continue
		if 'Exon' in alpha[0]:
			data = alpha[0].split(' ')
			if float(data[-1]) < 0.95:
				continue
		