for alpha in /home/vdp5/data/gene_finder/vir_all_ASM241v2/all_split/*; do
	genemame=$(basename -s .fasta $alpha)
	forward=$(tail -n+2 $alpha | head -n1)
	reverse=$(python /home/vdp5/scripts/get_complement.py -seq $forward)
	cd /home/vdp5/data/cdna_analysis_ASM241_v2/fasta_ASM241_v2
	forwardgrep=$(grep -i -r -l $forward *)
	reversegrep=$(grep -i -r -l $reverse *)
	printf "%s\t%s\t%s\n" "$forwardgrep" "$reversegrep"
done