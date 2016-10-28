import csv, os

input_data = list(csv.reader(open('/home/vdp5/data/gff_data/GCF_000002415.2_ASM241v2_genomic.gff'),delimiter='\t'))
outputdata = open('/home/vdp5/data/gff_data/GCF_000002415.2_ASM241v2_fakebed.bed', 'w')
input_data = [a for a in input_data if a[0][0] != '#']
newbedarray = []

for alpha in input_data:
	col1=alpha[0]
	col2=alpha[3]
	col3=alpha[4]
	col4=alpha[2]+ ';' + alpha[-1]
	col5='up'
	col6=alpha[6]
	col7='um'
	col8='uh'
	col9='uhhhhhh'
	col10='uhmmmm'
	col11='354,109,1189,'
	col12='0,739,1347,'

	lst = [col1, col2, col3, col4]
	newstr = '\t'.join(lst) + '\n'
	outputdata.write(newstr)


