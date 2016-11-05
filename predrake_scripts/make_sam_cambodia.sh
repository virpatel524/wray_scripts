newbase="/home/vdp5/data/cambodia_samples/sequences_sai/"
sai=".sai"
for file in /home/vdp5/data/cambodia_samples/sequences_raw/*; do
	IFS=/ read -a myarray <<< $file
	tmp_name=${myarray[-1]}
	IFS=. read -a newarray <<< $tmp_name
	filebase=${newarray[0]}
	newname=$newbase$filebase$sai
	bwa aln cambodia_test $file > $newname
done