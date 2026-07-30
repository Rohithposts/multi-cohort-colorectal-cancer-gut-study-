#!/usr/bin/python3
import os
os.system(
    "mkdir -p metaphlan_output_txt && "                      #creating output directory
    "mamba run -n metaphlan metaphlan --install"            #installing the database for analysis
)
with open("SRA_Accesion_list_PRJNA389927.txt") as f:
    for line in f:
        acc_id = line.strip()
        os.system(
            f"mamba run -n sra prefetch {acc_id} && "     #accessing the SRA, installing it, and converting it to .fastq
            f"mamba run -n sra fasterq-dump {acc_id} && "
            f"gzip {acc_id}_1.fastq && "
            f"gzip {acc_id}_2.fastq && "
            f"mamba run -n metaphlan metaphlan {acc_id}_1.fastq.gz,{acc_id}_2.fastq.gz --input_type fastq --tax_lev g -o metaphlan_output_txt/{acc_id}.txt && "              #running metaphlan analysis to generate taxa abundunce data (genus level) for the samples
            f"rm {acc_id}_1.fastq.gz && "
            f"rm {acc_id}_2.fastq.gz "                      #to prevent loss of disk space, deletign the .fastq files after the analysis is over
        )

os.system(                                                #merging the output to get a final table
    "mamba run -n metaphlan merge_metaphlan_tables.py metaphlan_output_txt/*.txt > PRJNA389927.tsv" 
)
