The aim of this study is to find patterns of taxa abundunce levels at genus level that are consistently associated with the gut samples of patients affected with colorectal cancer when compared with healthy samples within the same group across multiple cohorts. Different cohorts often have different hidden confounders acting affecting the reads generated (sequencing technology, geogrophy, diet and so on). The goal is to find patterns of taxa at genus level whose abundunce level changes when compared to healthy samples are consistently being associated with gut of colorectal cancer across different cohorts despite mutliple hidden confounders. 

These taxa are reported to only be ASSOCIATED with the gut of colorectal cancer among the sampels in the selected cohorts. There is no claim that these are "biomarkers" of colorectal cancer.

4 studies were selected such that each study has both healthy and affected samples. Any healthy vs cancer comparison was done within each study among the healthy and affected cancer samples within the same cohort. Comparing healthy and affected sampels from different cohorts will skew the results. Therefore, each study has both healthy and colorectal cancer affected samples. IMPORTANTLY, all the samples were not pooled into one big group to run the analyses. Each group/cohort was analysed separately.

Across all 4 datasets, a combined total of 453 samples (204 healthy and 231 colorectal cancer) were involved from the following NCBI BioProject IDs: PRJEB10878, PRJNA389927, PRJEB53415 and PRJEB36789. Among these, PRJEB36789 and PRJEB53415 are 16S Amplicon reads and the rest are WGS. Since 16S Amplicon reads cannot give accurate information at species/gene level, this analysis stopped at genus level. The 16S reads were analysed using QIIME2 and R while the WGS reads were screened using metaphlan.

In some of the BioProject IDs, along with healthy and colorectal cancer, gut reads of adenoma and orther such conditions are also present. From each BioProject, only healthy and colorectal cancer gut reads were slected.

For each of the output abundunce table from each study, MaAslin2 analysis was done to obtain the list of genus whose abundunce levels have changed and is statistically significant. The MaAslin2 output for each of the 4 cohorts can be accessed from the "MaAslin2_output_results" directory in this repository.
The .yml file to create and install the required conda environments and tools has also been added to the repository.
The code for the analysis for each study can be accessed from this repo. For each study, please run the script(s) "main_pipeline_...py" inside the folder itself using python3. For example:
```bash
(base) User@LAPTOP-XYZ123:~/multi-cohort-colorectal-cancer-gut-study-/PRJEB36789$ ls
PRJEB36789.R                  PRJEB36789_metadata.csv           main_pipeline_PRJEB36789_16S.py           qiime_manifest.py  
SRA_Accesion_list_PRJEB36789.txt              
(base) User@LAPTOP-XYZ123:~/multi-cohort-colorectal-cancer-gut-study-/PRJEB36789$ python3 main_pipeline_PRJEB36789_16S.py
```
The same holds for the final MaAslin2 analysis:
```bash
(base) User@LAPTOP-XYZ123:~/multi-cohort-colorectal-cancer-gut-study-/MaAslin2_analysis$ ls
MaAslin2_analysis.R             PRJEB10878_metadata.csv         PRJEB36789_metadata.csv         PRJEB53415_metadata.csv          PRJNA389927_metadata.csv
PRJEB10878_abundunce_table.tsv  PRJEB36789_abundance_table.tsv  PRJEB53415_abundance_table.tsv  PRJNA389927_abundunce_table.tsv
(base) User@LAPTOP-XYZ123:~/multi-cohort-colorectal-cancer-gut-study-/MaAslin2_analysis$ mamba run -n r Rscript MaAslin2_analysis.R
```
The analysis of the MaAslin2 output(s) is in "Analysis of the results.md".
