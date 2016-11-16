bowtie2 --no-discordant -D 20 -R 3 -N 1 -L 20  -x /home/vdp5/data/salvador_vivax_asia_2016/first-SAMEA2376790/SAMEA2376790 -1 /home/vdp5/data/cambodia_samples/sequences_gz/OM339-BiooBarcode43_TACAGC_R1.fastq.gz -2 /home/vdp5/data/cambodia_samples/sequences_gz/OM339-BiooBarcode43_TACAGC_R2.fastq.gz | samtools view  -Sb - | samtools sort - /home/vdp5/data/optimize_alignment_tests/OM339_rec_bowtie2.sorted

qualimap bamqc -bam /home/vdp5/data/optimize_alignment_tests/OM339_rec_bowtie2.sorted.bam -outdir /home/vdp5/data/optimize_alignment_test/OM339 -outfile bowtie_verysensitive.analysis.pdf -outformat pdf

