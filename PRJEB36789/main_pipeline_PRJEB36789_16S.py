#!/usr/bin/python
import os
from pathlib import Path
# downloading files from SRA, generating FASTQ files, and running FASTQC and MULTIQC
os.system(                                       #creating directories
    "mkdir -p $PWD/sra && "
    "mkdir -p $PWD/fastqfiles && "
    "mkdir -p $PWD/fastqc && "
    "mkdir -p $PWD/qiime_artifacts"
)

os.system(                              #installing silva classifier for V4 16S Amplicon [human stool]
    "wget https://www.arb-silva.de/fileadmin/silva_databases/current/QIIME2/2025.7/SSU/V4-515f-806r/weighted/human-stool/SILVA138.2_SSURef_NR99_weighted_classifier_V4-515f-806r_human-stool.qza && "
    "mv SILVA138.2_SSURef_NR99_weighted_classifier_V4-515f-806r_human-stool.qza $PWD/qiime_artifacts"
)
os.system(                              #downloading sra files
    "dos2unix SRA_Accesion_list_PRJEB36789.txt && "
    "cat SRA_Accesion_list_PRJEB36789.txt | parallel -j 4 'mamba run -n sra prefetch -p -O $PWD/sra'"
)
with open("SRA_Accesion_list_PRJEB36789.txt") as f:
    for line in f:
        sample_id = line.strip()
        os.system(                      #downloading sra files, generating fastq files and compressing them
            f"mamba run -n sra fasterq-dump $PWD/sra/{sample_id} -O $PWD/fastqfiles -p --split-3 && "
            f"gzip $PWD/fastqfiles/{sample_id}_1.fastq && "
            f"gzip $PWD/fastqfiles/{sample_id}_2.fastq"
        )

os.system(                               #running fastqc and multiqc
    "mamba run -n qc fastqc $PWD/fastqfiles/* -O $PWD/fastqc && "
    "mamba run -n qc multiqc $PWD/fastqc/ -o $PWD/"
)

os.system(                               #generating manifest to import into QIIME2
    "chmod +x $PWD/qiime_manifest.py && "
    "python3 $PWD/qiime_manifest.py -r $PWD/fastqfiles && "
    "mv $PWD/fastqfiles/manifest.tsv $PWD"
)

os.system(                               #importing into QIIME2 and removing primers
    "mamba run -n q2 qiime tools import --type 'SampleData[PairedEndSequencesWithQuality]' --input-path $PWD/manifest.tsv --output-path $PWD/qiime_artifacts/import.qza --input-format PairedEndFastqManifestPairedEnd && "
    "mamba run -n q2 qiime cutadapt trim-paired --i-demultiplexed-sequences $PWD/qiime_artifacts/import.qza --p-front-f GTGYCAGCMGCCGCGGTAA --p-front-r GGACTACNVGGGTWTCTAAT --p-match-adapter-wildcards --p-discard-untrimmed --p-cores 14 --o-trimmed-sequences $PWD/qiime_artifacts/primers_removed.qza"
)

os.system(                               #denoising step to generate QIIME output artifacts for further analysis
    "mamba run -n q2 qiime dada2 denoise-paired --i-demultiplexed-seqs $PWD/qiime_artifacts/primers_removed.qza --p-trunc-len-f 145 --p-trunc-len-r 145 --p-trim-left-f 0 --p-trim-left-r 0 --o-table $PWD/qiime_artifacts/table.qza --o-representative-sequences $PWD/qiime_artifacts/seqs.qza --o-denoising-stats $PWD/qiime_artifacts/stats.qza --p-n-threads 10"
)

os.system(                               #taxonomy classification
    "mamba run -n q2 qiime feature-classifier classify-sklearn --i-reads $PWD/qiime_artifacts/seqs.qza --i-classifier $PWD/qiime_artifacts/SILVA138.2_SSURef_NR99_weighted_classifier_V4-515f-806r_human-stool.qza --p-n-jobs 10 --o-classification $PWD/qiime_artifacts/taxonomy_classification.qza"
)

os.system(                              #generating phylogenetic tree
    "mamba run -n q2 qiime phylogeny align-to-tree-mafft-fasttree --i-sequences $PWD/qiime_artifacts/seqs.qza --o-alignment $PWD/qiime_artifacts/alignedseqs.qza --o-masked-alignment $PWD/qiime_artifacts/masked-alignment.qza --o-tree $PWD/qiime_artifacts/unrootedtree.qza --o-rooted-tree $PWD/qiime_artifacts/rooted-tree.qza --p-n-threads 12"
)

os.system(
    "mamba run -n r Rscript PRJEB36789.R " 
    "$PWD/qiime_artifacts/table.qza "
    "$PWD/qiime_artifacts/taxonomy_classification.qza "
    "$PWD/qiime_artifacts/rooted-tree.qza "
    "$PWD/qiime_artifacts/seqs.qza "
    "$PWD/PRJEB36789_metadata.csv"
)
