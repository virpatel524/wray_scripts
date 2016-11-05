echo "complete" > stampcomplete/plasmo13_prot_blastdb
cd $OUTPUT2
makeblastdb -in $INPUT0 -parse_seqids -dbtype prot
