import os, sys, csv, argparse


parser = argparse.ArgumentParser();
parser.add_argument('-seqfile')
parser.add_argument('-outdir')
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



outdir = args['outdir']
for chrom in chrom2items:

