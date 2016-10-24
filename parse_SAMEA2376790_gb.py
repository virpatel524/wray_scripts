import Bio
from Bio import SeqIO
import os



for filename in os.listdir('/home/vdp5/data/gene_finder/SAMEA2376790_genbank/SAMEA2376790_gb/'):
	chromname =  filename.split('.')[0]
	gb_file_test = os.path.join('/home/vdp5/data/gene_finder/SAMEA2376790_genbank/SAMEA2376790_gb', filename)
	fullpathnew = os.mkdir(os.path.join('/home/vdp5/data/gene_finder/vir_bychrom', chromname))
	os.chdir(os.path.join('/home/vdp5/data/gene_finder/vir_bychrom', chromname))
	data = SeqIO.read(open(gb_file_test,"r"), "genbank")
	for alpha in data.features:
		tmp =  alpha.qualifiers
		if 'product' in tmp:
			if 'VIR' in tmp['product'][0]:
				sequence =  alpha.extract(data.seq)
				output_fle = open('%s_%s.fasta' %(tmp['locus_tag'][0], chromname), 'w')
				output_fle.write('>%s | %s\n' %(tmp['locus_tag'][0], chromname))
				output_fle.write('%s\n' %(sequence))
				output_fle.close()



