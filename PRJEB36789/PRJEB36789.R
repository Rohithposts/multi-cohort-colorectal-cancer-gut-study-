args <- commandArgs(trailingOnly = TRUE)

table <- args[1]
taxonomy <- args[2]
tree <- args[3]
seqs <- args[4]
metadata <- args[5]

install.packages(file2meco)
install.packages(microeco)
install.packages(phyloseq)
install.packages(qiime2R)
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

