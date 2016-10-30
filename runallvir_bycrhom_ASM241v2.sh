iterarray=(  01 02 03 04 05 06 07 08 09 10 11 12 13 14  )
for alpha in ${iterarray[@]}; do
	for beta in /home/vdp5/data/gene_finder/vir_bychrom_ASM241v2/*/; do
		for delta in $beta*; do

			if [[ $deleta == *"fuck"* ]]
			then
				continue
			fi

			# cd /home/vdp5/data/cdna_analysis_SAMEA2376790/vir_genes
			# IFS=/ read -ra newarray <<< $delta
			# IFS=. read -ra newerarray <<< ${newarray[-1]}
			# IFS=_ read -ra chromarray <<< ${newerarray[0]}
			# chrom=${chromarray[-1]}
			# mkdir ${newerarray[0]}
			# cd ${newerarray[0]}
			# splign -query $delta -subj /home/vdp5/data/cdna_analysis_SAMEA2376790/fasta_PV01/$chrom.fasta -aln ${newerarray[0]}_splign
		done
	done
done