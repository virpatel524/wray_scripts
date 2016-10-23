NEWDIR=/home/vdp5/data/other_country_vivax_genomes/sam
SRADIR=/home/vdp5/data/other_country_vivax_genomes/scratch/korea
SRADIRINDIA=/home/vdp5/data/other_country_vivax_genomes/scratch/india
cd $NEWDIR

stampy.py -o KOREA.sam -f sam --substitutionrate=0.05 -g /home/vdp5/data/salvador_vivax/salvador.fasta -h /home/vdp5/data/salvador_vivax/salvador.fasta -M $SRADIR/SRR332559_1.fastq $SRADIR/SRR332559_2.fastq $SRADIR/SRR332560_1.fastq $SRADIR/SRR332560_2.fastq $SRADIR/SRR332561_1.fastq $SRADIR/SRR332561_2.fastq $SRADIR/SRR332562_1.fastq $SRADIR/SRR332562_2.fastq $SRADIR/SRR332563_1.fastq $SRADIR/SRR332563_2.fastq $SRADIR/SRR332564_1.fastq $SRADIR/SRR332564_2.fastq $SRADIR/SRR332565_1.fastq  $SRADIR/SRR332565_2.fastq $SRADIR/SRR332566_1.fastq $SRADIR/SRR332566_2.fastq $SRADIR/SRR340091_1.fastq $SRADIR/SRR340091_2.fastq  > $LOGDIR/KOREA_align_log.txt
stampy.py -o INDIA.sam -f sam --substitutionrate=0.05 -g /home/vdp5/data/salvador_vivax/salvador.fasta -h /home/vdp5/data/salvador_vivax/salvador.fasta -M $SRADIR/SRR332912_1.fastq $SRADIR/SRR332912_2.fastq $SRADIR/SRR332913_1.fastq $SRADIR/SRR332913_2.fastq $SRADIR/SRR332914_1.fastq $SRADIR/SRR332914_2.fastq $SRADIR/SRR332915_1.fastq $SRADIR/SRR332915_2.fastq > $LOGDIR/INDIA_align_log.txt


# what is going on rn emacs test
