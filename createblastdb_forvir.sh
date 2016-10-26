cd /home/vdp5/data/gene_finder/vir_bychrom_SAMEA2376790/allvir_blastdb
makeblastdb -in allgenes.fasta -parse_seqids -dbtype nucl
cd /home/vdp5/data/gene_finder/vir_bychrom_SAMEA2376790/allvir_protblastdb
makeblastdb -in allprot.fasta -parse_seqids -dbtype prot 
