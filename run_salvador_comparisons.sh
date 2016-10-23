bash /home/vdp5/scripts/salvador_align_scripts/fastqgz_to_sam_cambodia__salvador1.sh &
bash /home/vdp5/scripts/salvador_align_scripts/fastqgz_to_sam_cambodia__salvador2.sh &
wait

BAM=/home/vdp5/data/cambodia_samples/salvador_align
FINAL=/home/vdp5/data/cambodia_samples/bam_align_quality_salvador

for file in $BAM/*; do
	filename=${file##*/}
	IFS=. read -a newarray <<< $filename
	basecase=${newarray[0]}
	mkdir $FINAL/$basecase
	qualimap bamqc -bam $file -outdir $FINAL/$basecase -outfile $basecase.analysis.pdf -outformat pdf

