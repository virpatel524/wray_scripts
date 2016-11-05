echo "complete" > stampcomplete/plasmo13_prot_blastdb
cd $OUTPUT3
makeblastdb -in $INPUT0 -parse_seqids -dbtype prot
