args <- commandArgs(trailingOnly = TRUE)

table <- args[1]
taxonomy <- args[2]
tree <- args[3]
seqs <- args[4]
metadata <- args[5]

if (!requireNamespace("remotes", quietly = TRUE)) {
    install.packages("remotes", repos="https://cloud.r-project.org")
}

if (!requireNamespace("BiocManager", quietly = TRUE)) {
    install.packages("BiocManager", repos="https://cloud.r-project.org")
}

if (!requireNamespace("file2meco", quietly = TRUE)) {
    remotes::install_github("ChiLiubio/file2meco")
}

if (!requireNamespace("qiime2R", quietly = TRUE)) {
    remotes::install_github("jbisanz/qiime2R")
}

if (!requireNamespace("microeco", quietly = TRUE)) {
    install.packages("microeco", repos="https://cloud.r-project.org")
}

if (!requireNamespace("phyloseq", quietly = TRUE)) {
    BiocManager::install("phyloseq", ask = FALSE)
}

library(file2meco)
library(microeco)
library(phyloseq)
library(qiime2R)

dataset <- qiime2meco(
  feature_table = table,
  sample_table = metadata,
  taxonomy_data = taxonomy,
  phylo_tree = tree,
  rep_fasta = seqs
)
x <- read_qza(table)
y <- x$data
z <- read.csv(metadata)
rownames(z) <- colnames(y)
dataset$filter_pollution(taxa = c('mitochondria', 'chloroplast'))
dataset$tidy_dataset()
norm <- meco2phyloseq(dataset_rar)
norm_rar <- rarefy_even_depth(norm, rngseed = T)
dataset_ps <- tax_glom(norm_rar, taxrank = "Genus")
otu_table(dataset_ps)


final_table <- as.data.frame(otu_table(dataset_ps))
write.csv(final_table, file = "feature_table.csv",row.names = TRUE)

