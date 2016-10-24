iterarray=(  01 02 03 04 05 06 07 08 09 10 11 12 13 14  )
for alpha in $iterarray; do
	for beta in /home/vdp5/data/gene_finder/vir_bychrom/chrom$alpha/*; do
		cd /home/vdp5/data/cdna_analysis_SAMEA2376790/vir_genes
		IFS=/ read -ra newarray <<< $beta
		echo ${newarray[-1]}
	done
done