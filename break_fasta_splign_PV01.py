import os
import csv

data = list(csv.reader(open('/home/vdp5/data/salvador_vivax_asia_2016/first-SAMEA2376790/pvivax_sal1_SAMEA2376790.fasta'),delimiter='\t'))

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




baes_new = '/home/vdp5/data/cdna_analysis_SAMEA2376790/fasta_PV01'

for alpha in chrom_dict:
	zeta = alpha.split(':')[1].split('.')[0]
	zeta = int(zeta)
	zeta = str(zeta)
	zeta = chrom + zeta.zfill(2)
	newfle = open(baes_new + '/' + zeta + '.fasta', 'w')
	newfle.write('%s\n' %(alpha))
	newfle.write('%s\n'%(chrom_dict[alpha]))
