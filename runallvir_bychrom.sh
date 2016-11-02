for vir in /home/vdp5/data/gene_finder/vir_all_ASM241v2/all_split/*; do
	genename=$(basename --suffix=.fasta $vir)
	splign -query $vir -subj /home/vdp5/data/cdna_analysis_ASM241_v2/fasta_full_exon_determine.fasta -aln 
done