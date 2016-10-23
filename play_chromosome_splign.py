import os
import csv

data = list(csv.reader(open('/home/vdp5/data/salvador_vivax_asia_2016/first-SAMEA2376790/pvivax_sal1_SAMEA2376790.fasta'),delimiter='\t'))

cur_chrome = 'beta'
chrom_dict = {}

for line in data:
	print line
	if line[0][0] == '>':
		cur_chrome = line[0]
	else:
		if cur_chrome not in chrom_dict:
			chrom_dict[cur_chrome] = line[0]
		else:
			chrom_dict[cur_chrome] = chrom_dict[cur_chrome] + line[0]


for key in chrom_dict:
	print len(chrom_dict[key])





