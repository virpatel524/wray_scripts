NEWDIR=/home/vdp5/data/other_country_vivax_genomes/sam
KOREA=/home/vdp5/data/other_country_vivax_genomes/fasta/gca-000320685.2-pv-n-korean-v1-genomic.fsa.fna
INDIA=/home/vdp5/data/other_country_vivax_genomes/fasta/gca-000320625.2-pv-india-vii-v2-genomic.fsa.fna

cd $NEWDIR

stampy.py -o KOREA.sam -f sam --substitutionrate=0.05 -g /home/vdp5/data/salvador_vivax/salvador.fasta -h /home/vdp5/data/salvador_vivax/salvador.fasta -M $KOREA > $LOGDIR/KOREA_align_log.txt
stampy.py -o INDIA.sam -f sam --substitutionrate=0.05 -g /home/vdp5/data/salvador_vivax/salvador.fasta -h /home/vdp5/data/salvador_vivax/salvador.fasta -M $INDIA > $LOGDIR/INDIA_align_log.txt