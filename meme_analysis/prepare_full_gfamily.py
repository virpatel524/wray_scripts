import csv, os, sys
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna



portillo_g = zip(*list(csv.reader(open('/home/vdp5/data/other_data/portillo_Gfamily.txt'),delimiter='\t')))[0]

lstnew = []



for alpha in portillo_g:
	try:
		tmp = list(csv.reader(open('/home/vdp5/data/gene_finder/vir_all_ASM241v2/all_split/{}.fasta'.format(alpha)),delimiter='\t'))
	except:
		continue
	lstnew = lstnew + tmp


outputfasta = open('/home/vdp5/data/gene_finder/vir_all_ASM241v2/portillo_g_all_dna.fasta','w')
outputprot = open('/home/vdp5/data/gene_finder/vir_all_ASM241v2/portillo_g_all_prot.fasta','w')


for alpha in lstnew:
	if alpha[0][0] == '>':
		outputfasta.write(alpha[0] + '\n')
		outputprot.write(alpha[0] + '\n')
	else:
		outputfasta.write(alpha[0] + '\n')
		prottmp = Seq(alpha[0], generic_dna)
		prottmp = prottmp.translate()
		outputprot.write(str(prottmp) + '\n')


outputprot.close()
outputfasta.close()
