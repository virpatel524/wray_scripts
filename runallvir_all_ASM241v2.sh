for delta in /home/vdp5/data/gene_finder/vir_all_ASM241v2/all_split/*; do
	cd /home/vdp5/data/cdna_analysis_ASM241_v2/prechromidsplign/spliceoutput
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

