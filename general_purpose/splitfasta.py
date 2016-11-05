import os, sys, csv, argparse


parser = argparse.ArgumentParser();
parser.add_argument('-seq')
parser.add_argument('-outfile')
args = parser.parse_args()
args = vars(args)

fulldata = list(csv.reader(open(args['seq']),delimiter='\t'))

curchrom = 'none'

chrom2items = {}
counter = 1;

for alpha in fulldata:
	if alpha[0][0] == '>':

		curchrom = alpha[0]
	else:
		chrom2items.setdefault(curchrom, []).append(alpha[0])

outfile = open(args['outfile'], 'w')

fullseq = ''

for key in chrom2items:
	seq = chrom2items[key]
	new = ''.join(seq)
	fullseq += new


outfile.write('>plasmodb13_splign_full\n')
outfile.write('{}\n'.format(fullseq))