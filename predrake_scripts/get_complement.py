import os, sys, csv, argparse

import Bio
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna

parser = argparse.ArgumentParser();
parser.add_argument('-seq')
args = parser.parse_args()
args = vars(args)
dna = Seq(args['seq'])
print dna.reverse_complement()