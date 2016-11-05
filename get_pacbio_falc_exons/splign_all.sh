for file in /home/vdp5/data/cambodia_samples/falcipurum_wray/transript_fasta_split/*; do
	genename=$(basename -s .fasta $file)
	splign -query $file -subj /home/vdp5/data/cambodia_samples/falcipurum_wray/plasmodb13_fullfasta_splign.fasta -aln /home/vdp5/data/falc_analysis_pacbio/splign_output/$genename.splign
done