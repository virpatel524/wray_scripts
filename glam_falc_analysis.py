import sys, os, argparse, csv

parser = argparse.ArgumentParser();
parser.add_argument('-exon1')
parser.add_argument('-exon2')
parser.add_argument('-targetproteins')
args = parser.parse_args()  
args = vars(args)

exon1fle = list(csv.reader(open(args['exon1']),delimiter='\t'))
exon2fle = list(csv.reader(open(args['exon2']),delimiter='\t'))
targetprotfle = list(csv.reader(open(args['targetprotiens']),delimiter='\t'))

exon1raw = args['exon1']
exon2raw = args['exon2']
exon3raw = args['exon3']




