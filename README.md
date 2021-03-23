# scripts-lab
all the scripts used in lab work
For calculating kmers in a given sequence, following scripts are required...
kmer_onlycount_for_sorting.py 
sort_kmer.sh
merging_dup.py
kmer_select_alphabatic.py

and to run the program following command should be used.
./run_kmer_count_sort inputfile kmer-size

it will generate a tab seperated kmer file ex: ahpc_nucleotide_seq_AL123456.txt_21_mer_merged.csv

to compare this kmer result with dsk kmer counting, command is..

python kmer_comparison_sort_dsk.py dsk_output_file kmer_count_sort_output_file

