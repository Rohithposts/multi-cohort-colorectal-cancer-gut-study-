args <- commandArgs(trailingOnly = TRUE)

table <- args[1]
taxonomy <- args[2]
tree <- args[3]
seqs <- args[4]
metadata <- args[5]

if (!requireNamespace("pak", quietly = TRUE)) {
  install.packages("pak")
}

pak::pkg_install(c(
  "bioc::phyloseq",
  "jbisanz/qiime2R",
  "ChiLiubio/file2meco",
  "ChiLiubio/microeco"
))

library(file2meco)
library(microeco)
library(phyloseq)
library(qiime2R)

dataset <- qiime2meco(
  feature_table = table,
  sample_table = metadata,
  taxonomy_table = taxonomy,
  phylo_tree = tree,
  rep_fasta = seqs
)
x <- read_qza(table)
y <- x$data
z <- read.csv(metadata)
rownames(z) <- colnames(y)
dataset$filter_pollution(taxa = c('mitochondria', 'chloroplast'))
dataset$tidy_dataset()
norm <- meco2phyloseq(dataset)
dataset_ps <- tax_glom(norm, taxrank = "Genus")


final_table <- as.data.frame(otu_table(dataset_ps))
tax_df <- as.data.frame(tax_table(dataset_ps))
genus_names <- tax_df[rownames(final_table), "Genus"]
rownames(final_table) <- genus_names
write.csv(final_table, file = "PRJEB53415_abundunce_table.csv",row.names = TRUE)
