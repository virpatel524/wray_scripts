import Bio
from Bio import SeqIO
import os
counter = 1
masterfle = open('/home/vdp5/data/gene_finder/vir_all_ASM241v2/allgenes.txt', 'w')
masterfle_prot = open('/home/vdp5/data/gene_finder/vir_all_ASM241v2/allgenes_prot.txt', 'w')




gb_file_test = '/home/vdp5/data/gene_finder/ASM241v2_genbank/GCA_000002415.2_ASM241v2_genomic.gb'
data = SeqIO.parse(gb_file_test, "genbank")

while 5 < 6:
	starter = next(data).features
	for alpha in starter:
		tmp = alpha.qualifiers
		if 'product' in tmp:
			if 'Vir' in tmp['product'][0]:
				sequence =  alpha.extract(starter.seq)
				print sequence

# for alpha in data.features:
# 	tmp =  alpha.qualifiers
# 	if 'product' in tmp:
# 		if 'Vir' in tmp['product'][0]:
# 			sequence =  alpha.extract(data.seq)
# 			print sequence
# 			protseq = alpha.extract(data.seq).translate()
# 			# prottrans = tmp['translation'][0]
# 			# print prottrans
# 			output_fle = open('%s_%s.fasta' %(tmp['locus_tag'][0], chromname), 'w')
# 			# output_fle_prot = open('%s_%s_prot.fasta' %(tmp['locus_tag'][0], chromname), 'w')

# 			output_fle.write('>%s | %s\n' %(tmp['locus_tag'][0], chromname))
# 			output_fle.write('%s\n' %(sequence))
# 			output_fle.close()


# 			# output_fle_prot.write('>%s | %s\n' %(tmp['locus_tag'][0], chromname))
# 			# output_fle_prot.write('%s\n' %(protseq))
# 			# output_fle_prot.close()

# 			masterfle.write('>%s_%s vir %d \n' %(tmp['locus_tag'][0], chromname, counter))
# 			masterfle.write('%s\n' %(sequence))

# 			masterfle_prot.write('>%s_%s vir %d \n' %(tmp['locus_tag'][0], chromname, counter))
# 			masterfle_prot.write('%s\n' %(protseq))


# 			counter += 1






masterfle.close()
masterfle_prot.close()
