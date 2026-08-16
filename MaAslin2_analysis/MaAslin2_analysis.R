pak::pak("biobakery/Maaslin2")

library(Maaslin2)

PRJEB36789_metadata <- read.csv(
    "PRJEB36789_metadata.csv",
    row.names = 1,
    check.names = FALSE
)

PRJEB53415_metadata <- read.csv(
    "PRJEB53415_metadata.csv",
    row.names = 1,
    check.names = FALSE
)

PRJNA389927_metadata <- read.csv(
    "PRJNA389927_metadata.csv",
    row.names = 1,
    check.names = FALSE
)

PRJEB10878_metadata <- read.csv(
    "PRJEB10878_metadata.csv",
    row.names = 1,
    check.names = FALSE
)


PRJEB36789_abundance <- read.delim(
    "PRJEB36789_abundunce_table.tsv",
    row.names = 1,
    check.names = FALSE
)

PRJEB53415_abundance <- read.delim(
    "PRJEB53415_abundunce_table.tsv",
    row.names = 1,
    check.names = FALSE
)

PRJNA389927_abundance <- read.delim(
    "PRJNA389927_abundunce_table.tsv",
    row.names = 1,
    check.names = FALSE
)

PRJEB10878_abundance <- read.delim(
    "PRJEB10878_abundunce_table.tsv",
    row.names = 1,
    check.names = FALSE
)

PRJEB36789_metadata <- PRJEB36789_metadata[
    colnames(PRJEB36789_abundance),
    ,
    drop = FALSE
]

PRJEB53415_metadata <- PRJEB53415_metadata[
    colnames(PRJEB53415_abundance),
    ,
    drop = FALSE
]

PRJNA389927_metadata <- PRJNA389927_metadata[
    colnames(PRJNA389927_abundance),
    ,
    drop = FALSE
]

PRJEB10878_metadata <- PRJEB10878_metadata[
    colnames(PRJEB10878_abundance),
    ,
    drop = FALSE
]

stopifnot(
    identical(
        colnames(PRJEB36789_abundance),
        rownames(PRJEB36789_metadata)
    )
)

stopifnot(
    identical(
        colnames(PRJEB53415_abundance),
        rownames(PRJEB53415_metadata)
    )
)

stopifnot(
    identical(
        colnames(PRJNA389927_abundance),
        rownames(PRJNA389927_metadata)
    )
)

stopifnot(
    identical(
        colnames(PRJEB10878_abundance),
        rownames(PRJEB10878_metadata)
    )
)

PRJEB36789 <- Maaslin2(
    input_data = PRJEB36789_abundance,
    input_metadata = PRJEB36789_metadata,
    output = "PRJEB36789_Maaslin2_analysis",
    fixed_effects = c("sample_type"),
    random_effects = NULL,
    normalization = "TSS",
    transform = "LOG",
    analysis_method = "LM"
)

PRJEB53415 <- Maaslin2(
    input_data = PRJEB53415_abundance,
    input_metadata = PRJEB53415_metadata,
    output = "PRJEB53415_Maaslin2_analysis",
    fixed_effects = c("sample_type"),
    random_effects = NULL,
    normalization = "TSS",
    transform = "LOG",
    analysis_method = "LM"
)

PRJNA389927 <- Maaslin2(
    input_data = PRJNA389927_abundance,
    input_metadata = PRJNA389927_metadata,
    output = "PRJNA389927_Maaslin2_analysis",
    fixed_effects = c("DiseaseClass"),
    random_effects = NULL,
    normalization = "NONE",
    transform = "LOG",
    analysis_method = "LM"
)

PRJEB10878 <- Maaslin2(
    input_data = PRJEB10878_abundance,
    input_metadata = PRJEB10878_metadata,
    output = "PRJEB10878_Maaslin2_analysis",
    fixed_effects = c("config"),
    random_effects = NULL,
    normalization = "NONE",
    transform = "LOG",
    analysis_method = "LM"
)