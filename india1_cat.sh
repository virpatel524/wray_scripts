for indfile in /home/vdp5/data/other_country_vivax_genomes/scratch/india/*_1*; do
	cat $infile >> /home/vdp5/data/other_country_vivax_genomes/india_1.txt
	rm -rf $infile
done
