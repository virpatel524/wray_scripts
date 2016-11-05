import sys, os, argparse, csv, shutil



def make_bash_file(temperatures, exonsraw, targetprotrwaw, outputdir):
	try: 
		shutil.rmtree(outputdir)
	except:
		pass
	try:
		os.mkdir(outputdir)
	except:
		pass

	for index, file in enumerate(exonsraw):
		os.mkdir(os.path.join(outputdir, 'exon{}'.format(index)))

	


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
