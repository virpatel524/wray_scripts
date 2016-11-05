import csv
import matplotlib
matplotlib.use('Agg')
import seaborn as sns


import matplotlib.pyplot as plt


data_fle_path = '../data/gff_align/india_gff_match.coords'
coord_data = list(csv.reader(open(data_fle_path),delimiter='\t'))[3:]
reference = coord_data[0]
rest_data = coord_data[1:]


percentages = [float(a[6]) for a in rest_data]


sns.distplot(percentages, kde=False)

plt.xlabel('Percentage Similarity')
plt.ylabel('Number of Alignments')

plt.savefig('../figures/gff_india_align_mummer_delta.pdf')