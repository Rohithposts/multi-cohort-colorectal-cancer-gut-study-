#!/usr/bin/python3
import os
os.system(
    "mkdir -p metaphlan_output_txt && "                      #creating output directory
    "mamba run -n metaphlan metaphlan --install"            #installing the database for analysis
)

with open("First_Batch_Healthy_PRJEB6070.py", "w") as f:
    f.write("""
#!/usr/bin/python3
import os
with open("SRA_Accesion_PRJEB6070_healthy_Batch_1.txt") as f:
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
""")

with open("Second_Batch_Healthy_PRJEB6070.py", "w") as f:
    f.write("""
#!/usr/bin/python3
import os
with open("SRA_Accesion_PRJEB6070_healthy_Batch_2.txt") as f:
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
""")


with open("First_Batch_Cancer_PRJEB6070.py", "w") as f:
    f.write("""
#!/usr/bin/python3
import os
with open("SRA_Accesion_PRJEB6070_Cancer_Batch_1.txt") as f:
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
""")

with open("Second_Batch_Cancer_PRJEB6070.py", "w") as f:
    f.write("""
#!/usr/bin/python3
import os
with open("SRA_Accesion_PRJEB6070_Cancer_Batch_2.txt") as f:
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
""")

os.system(
    "python3 First_Batch_Healthy_PRJEB6070.py & "
    "python3 Second_Batch_Healthy_PRJEB6070.py & "
    "python3 First_Batch_Cancer_PRJEB6070.py & "
    "python3 Second_Batch_Cancer_PRJEB6070.py & "
    "wait"
)
os.system(                                                #merging the output to get a final table
    "mamba run -n metaphlan merge_metaphlan_tables.py metaphlan_output_txt/*.txt > PRJEB6070.tsv" 
)






