import sys, os, argparse, csv, shutil
import subprocess


def parse_motif_file(dirpath, allmotiffle):
	relmotifbase = dirpath.split('/')[-1]

	curmotif = 'nope'
	fle = open(dirpath, 'r')
	motiffile = fle.readlines()
	fle.close()

	motif2vals = {}
	counter = 1
	for line in motiffile:
		if line[0:5] == 'Score':
			score = lines.split(' ')[1]
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


def make_bash_file(temperatures, exonsraw, targetprotrwaw, outputdir):
	coolpaths = []
	try: 
		shutil.rmtree(outputdir)
	except:
		pass
	try:
		os.mkdir(outputdir)
	except:
		pass

	for index, file in enumerate(exonsraw):
		os.mkdir(os.path.join(outputdir, 'exon{}'.format(index + 1)))

	newfle = open(os.path.join(outputdir, 'runscript.sh'), 'w')
	counter = 0
	for index, file in enumerate(exonsraw):
		for temp in temperatures:
			newfle.write('glam2 -O {}_{}temp -2 -r 20 -t {} p {} &\n'.format(os.path.join(outputdir, 'exon{}'.format(index + 1)), temp, temp, file))
			coolpaths.append('{}_{}temp'.format(os.path.join(outputdir, 'exon{}'.format(index + 1)), temp))
			if counter == 2:
				newfle.write('wait\n\n')
				counter = 0

	return coolpaths


def make_glam2scan_bash(coolpaths, outputdir, targetprot):

	newfle = open(os.path.join(outputdir, 'runglam2scan.sh'), 'w')
	counter = 1
	for path in coolpaths:
		for filename in os.listdir(path):
			if filename.endswith('.motif'):
				newname = filename.split('/')[-1].split('.')[0]
				try: 
					shutil.rmtree(os.path.join(path, newname + 'glam2scan'))
				except:
					pass
				try:
					os.mkdir(os.path.join(path, newname + 'glam2scan'))
				except:
					pass
				newfle.write('glam2scan -O {} p {} {}\n &'.format(os.path.join(path, newname + 'glam2scan'), filename, targetprot))

	processrun = subprocess.Popen(['bash {}'.format(os.path.join(outputdir, 'runglam2scan.sh'))])
	processrun.wait()

def inter_results(coolpaths, outputdir):
	masterdict = {}
	motifrnafile = open(os.path.join(outputdir, ))
	for path in coolpaths:
		for filename in os.listdir(path):
			if filename.endswith('.motif'):
				newname = filename.split('/')[-1].split('.')[0]
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











parser = argparse.ArgumentParser();
parser.add_argument('-exons', nargs='+')
parser.add_argument('-targetproteins')
parser.add_argument('-outputdir')
args = parser.parse_args()  
args = vars(args)


exonsraw = args['exons']
targetprotrwaw = args['targetproteins']
outputdir = args['outputdir']

temperatures = [0.11, 0.2, 0.4, 0.7, 1, 1.2, 1.4, 1.7, 2, 3, 5]

relevantpaths = make_bash_file(temperatures, exonsraw, targetprotrwaw, outputdir)
processrun = subprocess.Popen(['bash {}'.format(os.path.join(outputdir, 'runscript.sh'))])
processrun.wait() 


allmotiffle = open(os.path.join(outputdir, 'allmotifs_scores.txt'), 'w')

for path in relevantpaths:
	parse_motif_file(path, allmotiffle)

allmotiffle.close()



