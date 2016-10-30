import os
import csv

data = list(csv.reader(open(''),delimiter='\t'))

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




baes_new = ''

for alpha in chrom_dict:
	zeta = alpha.split(':')[1].split('.')[0]
	zeta = int(zeta)
	zeta = str(zeta)
	zeta = 'chrom' + zeta.zfill(2)
	newfle = open(baes_new + '/' + zeta + '.fasta', 'w')
	newfle.write('%s\n' %(alpha))
	newfle.write('%s\n'%(chrom_dict[alpha]))
