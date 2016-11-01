import os, sys, csv, argparse

parser = argparse.ArgumentParser();
parser.add_argument('-seq')
args = parser.parse_args()
print vars(args)