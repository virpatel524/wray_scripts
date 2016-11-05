for korfile in /home/vdp5/data/other_country_vivax_genomes/scratch/india/*_2*; do
	cat $infile >> /home/vdp5/data/other_country_vivax_genomes/india_2.txt
	rm -rf $infile
done
