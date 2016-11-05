import csv, os, args, sys

parser = argparse.ArgumentParser();
parser.add_argument('-fasta')
parser.add_argument('-outdir')
args = parser.parse_args()
args = vars(args)
fastadata = list(csv.reader(open(['fasta']),delimiter='\t'))
