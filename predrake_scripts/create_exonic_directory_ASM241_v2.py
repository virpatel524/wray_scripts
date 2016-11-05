import os
import csv




def create_indexable(chrom, fle):
	chromdata = list(csv.reader(open('/home/vdp5/data/gene_finder/vir_bychrom_ASM241v2/{}/{}'.format(chrom, fle)),delimiter='\t'))
	stringineed = chromdata[-1][0]
	return stringineed


exitfle = open('/home/vdp5/data/cdna_analysis_ASM241_v2/gene2exon_ASM241_v2.txt', 'w')
rootdir = '/home/vdp5/data/cdna_analysis_ASM241_v2/vir_genes'
flag_file = open('/home/vdp5/data/cdna_analysis_ASM241_v2/flagged_genes.txt', 'w')

gene2exons = {}

for subdir, dirs, files in os.walk(rootdir):
	sortedfles = sorted(files)
	if len(sortedfles)!=2:
		continue
	tmp = list(csv.reader(open(os.path.join(subdir, sortedfles[0])),delimiter='\t'))
	holder = sortedfles[0][:-7].split('_')[-2:]
	chrom_file_search = '_'.join(holder)
	fastaname = sortedfles[0][:-7] + '.fasta'
	chrombyindex = create_indexable(chrom_file_search, fastaname)
	gene='_'.join(sortedfles[0].split('_')[:2])
	exonnums = []
	tmplst = []
	for alpha in tmp:
		if len(alpha) == 0: continue
		if 'Exon' in alpha[0]:
			data = alpha[0].split(' ')
			if float(data[-1]) < 0.95:
				continue
			indices =  [int(a) for a in data[3].split('(')[-1].split(',')[0].split('-')]
			tmplst.append('>{}_exon{}\n{}'.format(gene, data[2], chrombyindex[indices[0]-1:indices[1]]))

			exonnums.append(int(data[2]))
	tmplst = sorted(tmplst)
	if len(tmplst) != len(list(set(exonnums))):
		flag_file.write('{}\n'.format(gene))
		continue
	exitfle.write('\n'.join(tmplst) + '\n')


exitfle.close()
flag_file.close()
