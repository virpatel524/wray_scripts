import argparse, csv, sys

csv.field_size_limit(sys.maxsize)

parser = argparse.ArgumentParser();

parser.add_argument('filename', metavar='Name',type=str,nargs=2);
args = parser.parse_args()
arg_dict = vars(args)

first_data = list(csv.reader(open(arg_dict['filename'][0]),delimiter='\t'))
second_data = list(csv.reader(open(arg_dict['filename'][1]),delimiter='\t'))

first_data = [a for a in first_data if '#'!=a[0][0]]

chrom2index2nuc = {}



for index, alpha in enumerate(second_data):
	if index % 2 == 1: 
		continue

	tmp =  alpha[0].split(':')
	chrom = tmp[0][1:]
	nuc = second_data[index + 1][0]

	chrom2index2nuc.setdefault(chrom, {}).setdefault(tmp[1], nuc)




with open('../data/table_gff2nuc_plusID.txt', 'w') as newdfle:
	for alpha in first_data:
		chrom = alpha[0]
		if chrom not in chrom2index2nuc:
			continue
		indeces_option1 = '-'.join([str(int(alpha[3]) - 1), alpha[4]])
		indeces_option2 = '-'.join([str(int(alpha[3])), alpha[4]])

		int_which = 1;

		if indeces_option1 in chrom2index2nuc[chrom]:
			int_which = 1;
		elif indeces_option2 in chrom2index2nuc[chrom]:
			int_which = 2;
		else:
			continue

		which_ind = {}

		which_ind[1] = indeces_option1;
		which_ind[2] = indeces_option2;
			
		rest = alpha[-1].split(';')

		newdfle.write('>%s %s %s %s\n' %(rest[0].split('=')[-1], rest[1].split('=')[-1], rest[2].split('=')[-1], rest[-1].split('=')[-1], ))
		newdfle.write('%s\n' %(chrom2index2nuc[chrom][which_ind[int_which]]))

