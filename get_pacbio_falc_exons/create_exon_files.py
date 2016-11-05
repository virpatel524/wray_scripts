import csv
import os
import sys

input_dir_fasta = '/home/vdp5/data/cambodia_samples/falcipurum_wray/transript_fasta_split'
input_dir_splign = '/home/vdp5/data/falc_analysis_pacbio/splign_output'
exitfle = open('/home/vdp5/data/falc_analysis_pacbio/all_exons_plasmodb13.fasta', 'w')



def gene2seq(gene, exonchar):
	geneseq = list(csv.reader(open(input_dir_fasta +  '/{}.fasta'.format(gene)),delimiter='\t'))[1]
	coord = exonchar.split(':')[-1].split('-')
	if int(coord[0]) > int(coord[1]):
		return 'fail'
	return geneseq[0][int(coord[0]) - 1: int(coord[1])]

def newexonformat(tmplst, gene,fle):
	writer = ''
	for exon in tmplst:
		holder = gene2seq(gene, exon)
		if holder == 'fail':
			return

		writer+='>{}_{}\n{}\n'.format(gene, exon.split(':')[0], holder)

	fle.write(writer)

	return 


def process_data(alpha_data):
	tmplst = []
	for alpha in tmp:
		if len(alpha) == 0: continue
		if 'Exon' in alpha[0]:
			data = alpha[0].split(' ')
			tmplst.append(['exon{}:{}'.format(data[2], data[3].split('(')[-1].split(',')[0]), float(data[-1]), float(data[2])])

	repeatdict = {}
	for alpha in tmplst:
		repeatdict.setdefault(alpha[-1],[]).append([alpha[0], alpha[1]])


	exondata = []
	for exon in repeatdict:
		lst = repeatdict[exon]
		lst = sorted(lst, key=lambda x: x[-1])
		exondata.append(lst[0][0])
	return exondata




for subdir, dirs, files in os.walk(input_dir_splign):
	for splignout in files:
		tmp = list(csv.reader(open(os.path.join(input_dir_splign, splignout)),delimiter='\t'))
		gene=splignout.split('.')[0]
		tmplst = process_data(tmp)

		tmplst = sorted(tmplst)
		newexonformat(tmplst, gene, exitfle)
exitfle.close()
