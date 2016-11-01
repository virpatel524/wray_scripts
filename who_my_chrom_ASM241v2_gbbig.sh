for alpha in /home/vdp5/data/gene_finder/vir_all_ASM241v2/all_split/*; do
	genemame=$(basename -s .fasta $alpha)
	forward=$(tail -n+2 $alpha | head -n1)
	reverse=$(python /home/vdp5/scripts/get_complement.py -seq $forward)
	echo $reverse
done