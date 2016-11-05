

for korfile in /home/vdp5/data/other_country_vivax_genomes/scratch/korea/*_2*; do
	cat $korfile >> korea_2.txt
	rm -rf korfile
done
