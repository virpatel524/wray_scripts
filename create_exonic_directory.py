import os
import csv

rootdir = '/home/vdp5/data/cdna_analysis_SAMEA2376790/vir_genes'

for subdir, dirs, files in os.walk(rootdir):
	sortedfles = sorted(files)
	if len(sortedfles)!=2:
		continue
	tmp = list(csv.reader(open(sortedfles[0]),delimiter='\t'))
	print tmp
