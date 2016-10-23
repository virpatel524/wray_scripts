import os
import csv


data = list(csv.reader(open('/home/vdp5/data/gene_finder/origin_sequences/all_archive/all_origin.gb'),delimiter='\t'))
chrom2seq = {}

currchrom = 'fuck it'
for alpha in data:
	if "DEFINITION" in alpha[0]:
		tmp = alpha[0][-2:].split(' ')[-1]
		currchrom = 'chrom' + tmp.zfill(2)
	try:
		zeta = alpha[0].split(' ')

		zeta = [a for a in zeta if a != '']
		if currchrom == 'fuck it':
			print int(zeta[0])
			print zeta
		int(zeta[0])
		if '.' in alpha[0]:
			continue
		chrom2seq.setdefault(currchrom, []).append(alpha[0])
	except:
		continue


base = '/home/vdp5/data/gene_finder/origin_sequences/splitup/'

for alpha in chrom2seq:
	output = base + alpha + '.txt'
	newfle = open(output, 'w')
	newfle.write('\n'.join(chrom2seq[alpha]))
	newfle.write('\n')
	newfle.close()

