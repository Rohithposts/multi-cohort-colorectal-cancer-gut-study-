#!/usr/bin/python3

import os


with open("q2.yml", "w") as f:
    f.write("""name: q2

channels:
  - qiime2
  - conda-forge
  - bioconda

dependencies:
  - qiime2=2025.4
""")


with open("qc.yml", "w") as f:
    f.write("""name: qc

channels:
  - conda-forge
  - bioconda

dependencies:
  - fastqc=0.12.1
  - multiqc=1.35
  - python=3.12
""")


with open("sra.yml", "w") as f:
    f.write("""name: sra

channels:
  - conda-forge
  - bioconda

dependencies:
  - sra-tools=3.4.1
  - python=3.12
""")


with open("r.yml", "w") as f:
    f.write("""name: r

channels:
  - conda-forge
  - bioconda

dependencies:
  - r-base=4.6.1
  - r-pak
  - python=3.12
""")


with open("base-tools.yml", "w") as f:
    f.write("""name: base-tools

channels:
  - conda-forge
  - bioconda

dependencies:
  # Python
  - python=3.12
  - pip

  # Download tools
  - wget
  - curl
  - aria2
  - rsync
  - openssh

  # Compression
  - gzip
  - bzip2
  - xz
  - zstd
  - unzip
  - zip
  - pigz
  - p7zip

  # GNU utilities
  - coreutils
  - findutils
  - grep
  - sed
  - gawk
  - diffutils
  - patch
  - less
  - file
  - tree
  - which
  - time

  # Shell utilities
  - bash
  - bash-completion
  - parallel
  - dos2unix
  - tmux
  - screen

  # Build tools
  - make
  - cmake
  - pkg-config
  - autoconf
  - automake
  - libtool
  - m4
  - gcc
  - gxx
  - gfortran

  # Libraries commonly required when compiling R packages
  - zlib
  - bzip2
  - xz
  - zstd
  - liblzma-devel
  - libzlib
  - openssl
  - libcurl
  - libxml2
  - icu
  - readline
  - ncurses
  - sqlite
  - pcre2

  # Image libraries
  - libpng
  - jpeg
  - tiff
  - freetype
  - fontconfig
  - cairo
  - pixman
  - harfbuzz
  - fribidi

  # Math libraries
  - openblas
  - lapack
  - blas

  # SSL / certificates
  - ca-certificates
  - certifi

  # Git
  - git
  - git-lfs

  # JSON/XML
  - jq
  - yq

  # Useful bioinformatics utilities
  - samtools
  - seqkit
  - csvtk
""")


with open("metaphlan.yml", "w") as f:
    f.write("""name: metaphlan

channels:
  - bioconda
  - conda-forge

dependencies:
  - metaphlan=3.0.14
""")


os.system(
    "conda env create -f q2.yml && "
    "conda env create -f qc.yml && "
    "conda env create -f sra.yml && "
    "conda env create -f r.yml && "
    "conda env create -f base-tools.yml && "
    "conda env create -f metaphlan.yml"
)
