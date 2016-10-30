iterarray=(  01 02 03 04 05 06 07 08 09 10 11 12 13 14  )
for alpha in ${iterarray[@]}; do
	for beta in /home/vdp5/data/gene_finder/vir_bychrom_ASM241v2/*/; do
		for delta in $beta*; do
			cd /home/vdp5/data/cdna_analysis_SAMEA2376790/vir_genes
			IFS=/ read -ra newarray <<< $delta
			IFS=fasta read -ra newerarray <<< ${newarray[-1]}
			fullname=${newerarray[0]}
			fullname=${fullname::-1}
			IFS=_ read -ra chromarray <<< ${newerarray[0]}
			chrom=${chromarray[-2]}_${chromarray[-1]}
			chrom=${chrom::-1}
			mkdir ${fullname}
			cd ${fullname}
			splign -query $delta -subj /home/vdp5/data/cdna_analysis_ASM241_v2/fasta_ASM241_v2/$chrom.fasta -aln ${fullname}_splign
		done
	done
done