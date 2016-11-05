import Bio
from Bio import SeqIO
from Bio.Alphabet import generic_dna

input_handle = open("/home/vdp5/data/salvador_vivax_asia_2016/first-SAMEA2376790/pvivax_shortid.fasta", "r")
output_handle = open("/home/vdp5/data/gene_finder/origin_sequences/all_archive/SAMEA2376790.gb", "w")

sequences = list(SeqIO.parse(input_handle, "fasta"))

#asign generic_dna or generic_protein
for seq in sequences:
  seq.seq.alphabet = generic_dna

count = SeqIO.write(sequences, output_handle, "genbank")

output_handle.close()
input_handle.close()
print "Coverted %i records" % count


