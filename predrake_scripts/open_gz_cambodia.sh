abovedir="/home/vdp5/data/cambodia_samples/sequences_tmp/"
finaldir="/home/vdp5/data/cambodia_samples/sequences_raw/"
ending=".fastq"
endingfasta=".fasta"
for file in /home/vdp5/data/cambodia_samples/sequences_gz/*; do
	IFS=/ read -a myarray <<< $file
	tmp_name=${myarray[-1]}
	IFS=. read -a newarray <<< $tmp_name
	base=${newarray[0]}
	gunzip -c $file > $abovedir$base$ending
	paste - - - - < $abovedir$base$ending | cut -f 1,2 | sed 's/^@/>/' | tr "\t" "\n" > $finaldir$base$endingfasta
	rm -rf $abovedir$base$ending




	
done