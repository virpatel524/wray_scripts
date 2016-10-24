import csv
import sys, os
import subprocess



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


current_number = 1
for alpha in range(1, len(item_dict.keys()) + 1):
	if alpha % 10 == 0:
		current_number+=1
	with open('cambodia_align_scripts/fastqgz_to_sam_cambodia_%d.sh' %(current_number), 'a') as abouttoputin:
		beta = item_dict.keys()[alpha - 1]	
		abouttoputin.write('bwa mem -M /home/vdp5/data/salvador_vivax_asia_2016/first-SAMEA2376790/pvivax_sal1_SAMEA2376790.fasta %s %s | samtools view  -Sb - | samtools sort - /home/vdp5/data/cambodia_samples/sequences_bam/%s.sorted.bam\n\n' %(item_dict[beta][0], item_dict[beta][1], beta.split('.')[0]))