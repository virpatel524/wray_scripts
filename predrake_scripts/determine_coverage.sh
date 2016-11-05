for i in /home/vdp5/data/cambodia_samples/sequences_sam/*; do
	filename=${i##*/}
	samtools sort -o /home/vdp5/data/cambodia_samples/sequences_bam/$filename.sorted.bam -O bam -T $filename $i
	java -jar /home/vdp5/executables/picard.jar CollectAlignmentSummaryMetrics R=/home/vdp5/data/salvador_vivax_asia_2016/first-SAMEA2376790/pvivax_sal1_SAMEA2376790.fasta I=/home/vdp5/data/cambodia_samples/sequences_bam/$filename.sorted.bam O=/home/vdp5/data/cambodia_samples/coverage_analysis/$filename.coverage
	rm -rf /home/vdp5/data/cambodia_samples/sequences_bam/$filename.sorted.bam
done

