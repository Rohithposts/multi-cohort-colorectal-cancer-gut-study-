library(Maaslin2)

PRJEB36789 <- Maaslin2(
    input_data = PRJEB36789_abundunce_table.csv,
    input_metadata = PRJEB36789_metadata.csv,
    output = "PRJEB36789_Maaslin2_analysis",
    fixed_effects = c("sample_type"),
    random_effetcs = NULL,
    normalisation = "TSS",
    transform = "LOG",
    analysis_method = "LM"
)

PRJEB53415 <- Maaslin2(
    input_data = PRJEB53415_abundunce_table.csv,
    input_metadata = PRJEB53415_metadata.csv,
    output = "PRJEB53415_Maaslin2_analysis",
    fixed_effects = c("sample_type"),
    random_effetcs = NULL,
    normalisation = "TSS",
    transform = "LOG",
    analysis_method = "LM"
)

PRJNA389927 <- Maaslin2(
    input_data = PRJNA389927_abundunce_table.csv,
    input_metadata = PRJNA389927_metadata.csv,
    output = "PRJNA389927_Maaslin2_analysis",
    fixed_effects = c("sample_type"),
    random_effetcs = NULL,
    normalisation = "TSS",
    transform = "LOG",
    analysis_method = "LM"
)

PRJEB10878 <- Maaslin2(
    input_data = PRJEB10878_abundunce_table.csv,
    input_metadata = PRJEB10878_metadata.csv,
    output = "PRJEB10878_Maaslin2_analysis",
    fixed_effects = c("sample_type"),
    random_effetcs = NULL,
    normalisation = "TSS",
    transform = "LOG",
    analysis_method = "LM"
)