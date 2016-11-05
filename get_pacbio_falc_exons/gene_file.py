import os
import csv
import sys



translatefile = open('/home/vdp5/data/cambodia_samples/falcipurum_wray/smallgenenametobig.txt','w')
outfile = open('/home/vdp5/data/cambodia_samples/falcipurum_wray/plasmodb13_transcript_readable.fasta','w')

data = list(csv.reader(open('/home/vdp5/data/cambodia_samples/falcipurum_wray/Results/Pfalciparum3D7_transcripts.fasta'),delimiter='\t'))

curchrom = 'none'

chrom2items = {}
counter = 1;

for alpha in data:
	if alpha[0][0] == '>':
		tmp = alpha[0].split('"')

		curchrom = '>' + tmp[1] + '\n'
	else:
		chrom2items.setdefault(curchrom, []).append(alpha[0])



for gene in chrom2items:
	chrom2items[gene] = ''.join(chrom2items[gene]) + '\n'

print len(chrom2items)

for gene in chrom2items:
	outfile.write(gene)
	outfile.write(chrom2items[gene])
	newfle = open('/home/vdp5/data/cambodia_samples/falcipurum_wray/transript_fasta_split/genenum{}.fasta'.format(counter),'w')
	newfle.write('>genenum{}\n'.format(counter))
	newfle.write(chrom2items[gene])
	translatefile.write('genenum{}\t{}\n'.format(counter, gene))
	newfle.close()
	counter+=1;


outfile.close()
translatefile.close()



