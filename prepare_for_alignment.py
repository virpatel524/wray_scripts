import csv
import sys, os

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
	with open('fastqgz_to_sam_cambodia_%d.sh' %(current_number), 'a') as abouttoputin:
		abouttoputin.write('cd /home/vdp5/data/cambodia_samples/sequences_sam\n')
		beta = item_dict.keys()[alpha - 1]	
		abouttoputin.write('stampy.py -o %s.sam -f sam --substitutionrate=0.05 -g /home/vdp5/data/salvador_vivax/salvador.fasta -h /home/vdp5/data/salvador_vivax/salvador.fasta -M %s %s > $LOGDIR/%s_align_log.txt\n' %(beta, item_dict[beta][0], item_dict[beta][1], beta))

