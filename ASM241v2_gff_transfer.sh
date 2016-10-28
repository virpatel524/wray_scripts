python /home/vdp5/scripts/gff3_to_bed_converter.py -q /home/vdp5/data/gff_data/GCF_000002415.2_ASM241v2_genomic.gff -o /home/vdp5/data/gff_data/GCF_000002415.2_ASM241v2_genomic_bedformat.bed
# line above is for inital processing



bedtools getfasta -fi /home/vdp5/data/vivax_2009/GCA_000002415.2_ASM241v2_genomic.fasta -fo /home/vdp5/data/gene_finder/ASM241v2_exongrab/ASM241v2_exons.fasta -bed /home/vdp5/data/gff_data/GCF_000002415.2_ASM241v2_genomic_bedformat.bed -split -name 