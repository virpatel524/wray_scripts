import csv, os

input_data = list(csv.reader(open('/home/vdp5/data/gff_data/GCF_000002415.2_ASM241v2_genomic.gff'),delimiter='\t'))

print input_data