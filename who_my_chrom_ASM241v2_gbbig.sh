for alpha in /home/vdp5/data/gene_finder/vir_all_ASM241v2/all_split/*; do
	genemame=$(basename -s .fasta $alpha)
	tail -n+2 $alpha | head -n1
done