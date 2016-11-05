import sys, os, argparse, csv

parser = argparse.ArgumentParser();
parser.add_argument('-exons')
parser.add_argument('-targetproteins')
args = parser.parse_args()  
args = vars(args)


exonsraw = args['exons']
print exonsraw
targetprotrwaw = args['targetproteins']

temperatures = [0.11, 0.2, 0.4, 0.7, 1, 1.2, 1.4, 1.7, 2, 3, 5]

