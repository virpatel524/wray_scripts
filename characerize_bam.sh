BAM=/home/vdp5/data/cambodia_samples/sequences_bam
FINAL=/home/vdp5/data/cambodia_samples/bam_align_quality

for file in $BAM/*; do
	filename=${file##*/}
	IFS=. read -a newarray <<< $filename
	basecase=${newarray[0]}
	mkdir $FINAL/$basecase
	qualimap bamqc -bam $file -outdir $FINAL/$basecase -outfile $basecase.analysis.pdf -outformat pdf


done