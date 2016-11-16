import sys, os, argparse, csv, shutil
import subprocess


def parse_motif_file(dirpath, allmotiffle):
	relmotifbase = dirpath.split('/')[-1]

	curmotif = 'nope'
	fle = open(os.path.join(dirpath, 'glam2.txt'), 'r')
	motiffile = fle.readlines()
	fle.close()

	motif2vals = {}
	counter = 1
	for line in motiffile:
		if line[0:5] == 'Score':
			score = line.split(' ')[1]
			curmotif = 'motifnumber_{}'.format(counter) + relmotifbase + '.motif'
			allmotiffle.write('{}\t{}\n'.format('motifnumber_{}'.format(counter) + relmotifbase, score))
			motif2vals.setdefault(curmotif, []).append(line)
			counter+=1;
		else:
			motif2vals.setdefault(curmotif, []).append(line)

	for motif in motif2vals:
		if motif == 'none':
			continue
		else:
			newfle = open(os.path.join(dirpath, motif), 'w')
			for line in motif2vals[motif]:
				newfle.write(line)

	return


def make_bash_file_glam2(temperatures, exonsraw, targetprotrwaw, outputdir, seq_type):
	coolpaths = []
	counter = 0
	newfle = open(os.path.join(outputdir, 'runscript_glam2_orig.sh'), 'w')
	for index, file in enumerate(exonsraw):
		for temp in temperatures:
			newfle.write('glam2 -O {}_{}temp -2 -t {} {} {} &\n'.format(os.path.join(outputdir, 'exon{}'.format(index + 1)), temp, temp, seq_type, file))
			coolpaths.append('{}_{}temp'.format(os.path.join(outputdir, 'exon{}'.format(index + 1)), temp))
			counter += 1
			if counter == 4:
				newfle.write('wait\n\n')
				counter = 0

	return coolpaths


def make_glam2scan_bash(coolpaths, outputdir, targetprot, seq_type):
	newfle = open(os.path.join(outputdir, 'runglam2scan.sh'), 'w')
	counter = 1

	for path in coolpaths:
		for filename in os.listdir(path):
			if filename.endswith('.motif'):
				newname = filename.split('/')[-1].split('.motif')[0]
				newfle.write('glam2scan -O {} -n 60 {} {} {}\n'.format(os.path.join(path, newname + 'glam2scan'), seq_type, os.path.join(path, filename), targetprot))


def inter_results(coolpaths, outputdir):
	masterdict = {}
	for path in coolpaths:
		for filename in os.listdir(path):
			if filename.endswith('.motif'):
				newname = filename.split('/')[-1].split('.motif')[0]
				readertmp = open(os.path.join(path, newname + 'glam2scan', 'glam2scan.txt'))
				readerdata = readertmp.readlines()[4:]
				readertmp.close()
				for line in readerdata:
					if line[0] == ' ':
						continue
					if line == '\n':
						continue
					linesplit = line.split(' ')[0]
					masterdict.setdefault(linesplit, []).append(newname)

	masterdictfle = open(os.path.join(outputdir, 'glam2scan_results_full.txt'), 'w')

	for gene in masterdict:
		masterdictfle.write('{}\t'.format(gene))
		masterdictfle.write('{}\n'.format('\t'.join(masterdict[gene])))

	masterdictfle.close()
	scoredata = list(csv.reader(open(os.path.join(outputdir, 'allmotifs_scores.txt')),delimiter='\t'))

	motif2score = {}

	for motif in scoredata:
		motif2score[motif[0]] = float(motif[1])



	rna2score = {}
	scorelst = []

	for rna in masterdict:
		curscored = float(sum([motif2score[a] for a in masterdict[rna]]))
		rna2score[rna] = curscored
		scorelst.append(curscored)

	scoremax = max(scorelst)

	for rna in rna2score:
		rna2score[rna] = rna2score[rna] / scoremax

	sortedrnas = sorted(rna2score.keys(), key= lambda x: len(masterdict[x]), reverse=True)

	sortedcandidates = open(os.path.join(outputdir, 'sorted_candidates.txt'), 'w')

	for rna in sortedrnas:
		sortedcandidates.write('{}\t{}\t{}\n'.format(rna, rna2score[rna], len(masterdict[rna])))



parser = argparse.ArgumentParser();
parser.add_argument('-exons', nargs='+')
parser.add_argument('-targetproteins')
parser.add_argument('-outputdir')
parser.add_argument('-seq_type')
args = parser.parse_args()  
args = vars(args)

seq_type = args['seq_type']
exonsraw = args['exons']
targetprotrwaw = args['targetproteins']
outputdir = args['outputdir']


# try: 
# 	shutil.rmtree(outputdir)
# except:
# 	pass
# try:
# 	os.mkdir(outputdir)
# except:
# 	pass

temperatures = [0.11, 0.2, 0.4, 0.7, 1, 1.2, 1.4, 1.7, 2, 3, 5]

relevantpaths = make_bash_file_glam2(temperatures, exonsraw, targetprotrwaw, outputdir, seq_type)
# subprocess.call('bash {}'.format(os.path.join(outputdir, 'runscript_glam2_orig.sh')).split())
allmotiffle = open(os.path.join(outputdir, 'allmotifs_scores.txt'), 'w')

for path in relevantpaths:
	parse_motif_file(path, allmotiffle)

allmotiffle.close()



make_glam2scan_bash(relevantpaths, outputdir, targetprotrwaw, seq_type)
processrun = subprocess.call('bash {}'.format(os.path.join(outputdir, 'runglam2scan.sh')).split())
inter_results(relevantpaths, outputdir)


