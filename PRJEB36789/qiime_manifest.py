#!/usr/bin/python3
from pathlib import Path
import os
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate manifest to import into qiime, will be generated in the same input directory")
    parser.add_argument("-r", "--reads_dir", help="Directory containing all the fastq files. (Default: Current directory)", default="./")
    args=parser.parse_args()

req_dir = Path(args.reads_dir)
forwardpaths = []
reversepaths = []
ids = []
with open("SRA_Accesion_list_PRJEB36789.txt") as f:
    for line in f:
        reqid = line.strip()
        ids.append(reqid)
        for file in req_dir.iterdir():
            if f"{reqid}_1" in file.name:
                filepath_f = os.path.abspath(file)
                forwardpaths.append(filepath_f)
            if f"{reqid}_2" in file.name:
                filepath_r = os.path.abspath(file)
                reversepaths.append(filepath_r)
with open("manifest.tsv", "w") as f:
    f.write("sample-id\tforward-absolute-filepath\treverse-absolute-filepath\n")
    for x in ids:
        for y in forwardpaths:
            for z in reversepaths:
                if x in y:
                    if x in z:
                        f.write(f"{x}\t{y}\t{z}\n")



