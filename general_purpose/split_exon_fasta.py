import csv, os, args, sys

parser = argparse.ArgumentParser();
parser.add_argument('-fasta')
parser.add_argument('-outdir')
args = parser.parse_args()
args = vars(args)
fastadata = list(csv.reader(open(args['fasta']),delimiter='\t'))
outdir = args['outdir']


gene2seq = {}
curgene = 'fadsjfkdsa'

for alpha in fastadata:
	if alpha[0][0] == '>':
		curgene = alpha[0] + '\n'
	else:
		gene2seq.setdefault(curgene, []).append(alpha[0])


for gene in gene2seq:
	gene2seq[gene] = ''.join(gene2seq[gene]) + '\n'


