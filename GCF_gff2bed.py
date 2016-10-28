import csv, os

input_data = list(csv.reader(open('/home/vdp5/data/gff_data/GCF_000002415.2_ASM241v2_genomic.gff'),delimiter='\t'))
print len(input_data)
input_data = [a for a in input_data if a[0][0] != '#']
newbedarray = []

for alpha in input_data:
	col1=input_data[0]
	col2=input_data[3]
	col3=input_data[4]
	col4=input_data[2]+ ';' + input_data[-1]
	col5='up'
	col6=input_data[6]
	col7='um'
	col8='uh'
	col9='uhhhhhh'
	col10='uhmmmm'
	col11='354,109,1189,'
	col12='0,739,1347,'

	
