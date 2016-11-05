import csv
import sys, os
import subprocess
import itertools



item_dict = {}

for filename in os.listdir('/home/vdp5/data/cambodia_samples/sequences_gz'):
	tag = filename.split('_')[-1].split('.')[0]
	other_stuff = filename.split('_')[:-1]
	sample_id = ''
	if '-' in other_stuff[0]:
		if '-' in other_stuff[0]:
			beta = other_stuff[0].split('-')
			if 'Bar' in beta[-1]:
				sample_id = beta[0]
			else:
				sample_id = ''.join(beta)

	item_dict.setdefault(sample_id, []).append(os.path.join('/home/vdp5/data/cambodia_samples/sequences_gz', filename))


klist = [5, 10, 15, 20, 50, 100]
lowerwlist = [50, 100, 150]
rlist = [0.5, 1.0, 1.5, 2.0]
dlist = [50, 100, 150]
clist = [50,100,150]

current_number = 1
for alpha in range(1, 11):
	if alpha % 10 == 0:
		current_number+=1
	if current_number != 1: break
	iterator = list(itertools.product(klist, lowerwlist, rlist, dlist, clist))
	for index, listsel in enumerate(iterator):
		print index, len(iterator)
		with open('/home/vdp5/scripts/cambodia_PV01_improve_align/fastqgz_to_sam_cambodia_%d_improve.sh' %(current_number), 'a') as abouttoputin:
			beta = item_dict.keys()[alpha - 1]	
			abouttoputin.write('bwa mem -M -k {} -w {} -r {} -d {} -c {} /home/vdp5/data/salvador_vivax_asia_2016/first-SAMEA2376790/pvivax_sal1_SAMEA2376790.fasta {} {} | samtools view  -Sb - | samtools sort - /home/vdp5/tmp/{}_k{}_w{}_r{}_d{}_c{}.sorted.bam\n'.format(listsel[0], listsel[1], listsel[2], listsel[3], listsel[4], item_dict[beta][0], item_dict[beta][1], beta.split('.')[0], listsel[0], listsel[1], listsel[2], listsel[3], listsel[4]))
			abouttoputin.write('qualimap bamqc -bam /home/vdp5/tmp/{}_k{}_w{}_r{}_d{}_c{}.sorted.bam -outdir /home/vdp5/data/cambodia_samples/bam_align_quality_testing_improve/{} -outfile {}.analysis.pdf -outformat pdf\n'.format(beta.split('.')[0], listsel[0], listsel[1], listsel[2], listsel[3], listsel[4], beta.split('.')[0], beta.split('.')[0]))
			abouttoputin.write('rm -rf /home/vdp5/tmp/{}_k{}_w{}_r{}_d{}_c{}.sorted.bam\n'.format(beta.split('.')[0], listsel[0], listsel[1], listsel[2], listsel[3], listsel[4], beta.split('.')[0], beta.split('.')[0]))

