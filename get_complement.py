import os, sys, csv, argparse

parser = argparse.ArgumentParser();

args = parser.parse_args()
print args.accumulate(args)