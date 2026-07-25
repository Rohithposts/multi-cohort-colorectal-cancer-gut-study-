#!/usr/bin/python
from pathlib import Path
import os
import argparse
import pandas as pd

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate manifest to import into qiime, will be generated in the same input directory")
    parser.add_argument("-r", "--reads_dir", help="Directory containing all the fastq files. (Default: Current directory)", default="./")
    args=parser.parse_args()

req_dir = Path(args.reads_dir)
sample_ids = []
forward_absolute_filepath = []
reverse_absolute_filepath = []
for file in req_dir.iterdir():
    if "_1.fastq" in file.name:
        sample_ids.append(file.name.split("_1")[0])
        forward_absolute_filepath.append(os.path.abspath(file))
    if "_2.fastq" in file.name:
        reverse_absolute_filepath.append(os.path.abspath(file))

headers = ["sample-id", "forward-absolute-filepath", "reverse-absolute-filepath"]
manifest = pd.DataFrame(
    "sample-id": list(sample_ids),
    "forward-absolute-filepath": list(forward_absolute_filepath),
    "reverse-absolute-filepath": list(reverse_absolute_filepath)
)

manifest.to_csv(f"{req_dir}/manifest.tsv", columns=headers, sep="\t", index=False)


