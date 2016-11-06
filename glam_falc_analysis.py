import sys, os, argparse, csv, shutil
import subprocess


def parse_motif_file(dirpath):

	relmotifbase = dirpath.split('/')[-1]

	curmotif = 'nope'
	fle = open(dirpath, 'r')
	motiffile = fle.readlines()
	fle.close()

	motif2vals = {}
	counter = 1
	for line in motiffile:
		if line[0:5] == 'Score':
			curmotif = 'motifnumber_{}'.format(counter) + relmotifbase + '.motif'
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
			newfle.write('glam2 -O {}_{}temp -2 -r 20 -t {} p {}\n'.format(os.path.join(outputdir, 'exon{}'.format(index + 1)), temp, temp, file))
			coolpaths.append('{}_{}temp'.format(os.path.join(outputdir, 'exon{}'.format(index + 1)), temp))
			if counter == 2:
				newfle.write('wait\n\n')
				counter = 0

	return coolpaths


def make_glam2scan_bash(coolpaths, outputdir):

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

for path in relevantpaths:
	parse_motif_file(path)



