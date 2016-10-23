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
			print line[0]
			chrom_dict[cur_chrome] = line[0]
		else:
			chrom_dict[cur_chrome] = chrom_dict[cur_chrome] + line[0]


for key in chrom_dict:
	print len(chrom_dict[key])

new_thing = '/home/vdp5/data/fasta_editing/consolidated_lines_vivax_SAMEA2376790.fasta'
newfle = open(new_thing, 'w')
for alpha in chrom_dict:
	newfle.write('%s\n' %(alpha))
	newfle.write('%s\n'%(chrom_dict[alpha]))

newfle.close()
new_thing = '/home/vdp5/data/fasta_editing/alltogehter.fasta'
newfle = open(new_thing, 'w')
for alpha in chrom_dict:
	newfle.write('%s'%(chrom_dict[alpha]))
newfle.write('\n')
newfle.close()

