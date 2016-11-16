import matplotlib
matplotlib.use('Agg')

import sys, os, csv
import matplotlib.pylab as plt
import seaborn


def cleanupfasta(lst):
	masterdict = {}
	curgene = ''

	for alpha in lst:
		if alpha[0][0] == '>':
			curgene = alpha[0]
			continue
		else:
			masterdict.setdefault(curgene, []).append(alpha[0])

	for alpha in masterdict:
		masterdict[alpha] = ''.join(masterdict[alpha])

	return masterdict



var1 = list(csv.reader(open('/home/vdp5/data/hhmm_data/diana_analysis_var_prot_toitself/diana_analysis_var_prot_toitselfsorted_candidates.txt'),delimiter='\t'))
var2 = list(csv.reader(open('/home/vdp5/data/hhmm_data/diana_analysis_var_prot_plasmodb/diana_analysis_var_prot_plasmodbsorted_candidates.txt'),delimiter='\t'))
rif1 = list(csv.reader(open('/home/vdp5/data/hhmm_data/diana_analysis_rif_prot_toitself/diana_analysis_rif_prot_toitselfsorted_candidates.txt'),delimiter='\t'))
rif2 = list(csv.reader(open('/home/vdp5/data/hhmm_data/diana_analysis_rif_prot_plasmodb/diana_analysis_rif_prot_plasmodbsorted_candidates.txt'),delimiter='\t'))
stevor1 = list(csv.reader(open('/home/vdp5/data/hhmm_data/diana_analysis_stevor_prot_toitself/diana_analysis_stevor_prot_toitselfsorted_candidates.txt'),delimiter='\t'))
stevor2 = list(csv.reader(open('/home/vdp5/data/hhmm_data/diana_analysis_stevor_prot_plasmodb/diana_analysis_stevor_prot_plasmodbsorted_candidates.txt'),delimiter='\t'))

varthresh = 0.02
rifthresh = 0.02
stevorthresh = 0.10

toitself_var = list(csv.reader(open('/nfs/wraycompute/diana/var/var_falciparum_aa.fa'),delimiter='\t'))
plasmodbprots = list(csv.reader(open('/home/vdp5/data/cambodia_samples/falcipurum_wray/Results/Pfalciparum3D7_proteins.fasta'),delimiter='\t'))
toitself_var = cleanupfasta(toitself_var)
plasmodbprots = cleanupfasta(plasmodbprots)

var_itself_genesinterest = []
var_plasmodb_genesinterest = []

for alpha in var1:
	if float(alpha[1]) > varthresh:
		var_itself_genesinterest.append(alpha[0])

for alpha in var2:
	if float(alpha[1]) > varthresh:
		var_plasmodb_genesinterest.append(alpha[0])



varselfinterest = open('/home/vdp5/data/hhmm_data/diana_analysis_var_meme/varitselfinterest.fasta', 'w')

for alpha in var_itself_genesinterest:
	matches = []
	for beta in toitself_var:
		if alpha in beta:
			matches.append(beta)

	varselfinterest.write('>' + alpha + '\n')
	varselfinterest.write(toitself_var[matches[0]] + '\n')



plasmodbinterests = open('/home/vdp5/data/hhmm_data/diana_analysis_var_meme/plasmodbinterests.fasta', 'w')

for alpha in var_plasmodb_genesinterest:
	matches = []
	for beta in plasmodbprots:
		if alpha in beta:
			matches.append(beta)

	plasmodbinterests.write('>' + alpha + '\n')
	plasmodbinterests.write(plasmodbprots[matches[0]] + '\n')

bashscript = open('makemotifs.sh', 'w')

bashscript.write('meme /home/vdp5/data/hhmm_data/diana_analysis_var_meme/varitselfinterest.fasta -oc /home/vdp5/data/hhmm_data/diana_analysis_var_meme_analysis  -maxsize 450000 -mod zoops -nmotifs 5')

