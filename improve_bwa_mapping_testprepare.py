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


klist = [5, 10, 15, 20, 30, 50, 100]
lowerwlist = [25, 50, 100, 150, 200]
rlist = [0.25, 0.5, 1.0, 1.5, 1.75, 2.0]
dlist = [25, 50, 100, 150, 200]
clist = [0,25,50,100,150,200]

current_number = 1
for alpha in range(1, len(item_dict.keys()) + 1):
	if alpha % 10 == 0:
		current_number+=1
		if current_number != 1: break
	iterator = list(itertools.product(klist, lowerwlist, rlist, dlist, clist))
	for index, listsel in enumerate(iterator):
		print index, len(iterator)
		with open('/home/vdp5/scripts/cambodia_PV01_improve_align/fastqgz_to_sam_cambodia_%d_improve.sh' %(current_number), 'a') as abouttoputin:
			beta = item_dict.keys()[alpha - 1]	
			abouttoputin.write('bwa mem -M -k {} -w {} -r {} -d {} -c {} /home/vdp5/data/salvador_vivax_asia_2016/first-SAMEA2376790/pvivax_sal1_SAMEA2376790.fasta {} {} | samtools view  -Sb - | samtools sort - /home/vdp5/data/cambodia_samples/sequences_bam/{}_k{}_w{}_r{}_d{}_c{}.sorted.bam\n\n'.format(listsel[0], listsel[1], listsel[2], listsel[3], listsel[4], item_dict[beta][0], item_dict[beta][1], listsel[0], listsel[1], listsel[2], listsel[3], listsel[4], beta.split('.')[0]))