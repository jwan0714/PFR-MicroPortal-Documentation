# nf-core/rnaseq on powerPlant: Usage
#### Author: Jack Wang
## Table of contents


<!-- Install Atom plugin markdown-toc-auto for this ToC to auto-update on save -->
<!-- TOC START min:2 max:3 link:true asterisk:true update:true -->
* [Table of contents](#table-of-contents)
* [Introduction](#introduction)
  * [What's nf-core](#What's-nf-core)
  * [What's Nextflow](#What's-Nextflow)
  * [What's nf-core/rnaseq](#What's-nf-core/rnaseq)
* [Installation](#Installation)
  * [powerPlant usage](#powerPlant-usage)
  * [Installation preparation](#Installation-preparation)
  * [Nextflow Installation](#Nextflow-Installation)
  * [nf-core Installation](#nf-core-Installation)  
* [Pipeline configuration & pre-running setup](#Pipeline-configuration-&-pre-running-setup)
  * [Pipeline configuration](#Pipeline-configuration)
  * [Reference genomes](#Reference-genomes)
  * [Pre-running setup](#Pre-running-setup)
* [Running the pipeline](#running-the-pipeline)
  * [Reproducibility](#reproducibility)
* [Main arguments](#main-arguments)
  * [`-profile`](#-profile)
  * [`--reads`](#--reads)
  * [`--singleEnd`](#--singleend)
  * [Library strandedness](#library-strandedness)
* [FeatureCounts Extra Gene Names](#featurecounts-extra-gene-names)
  * [Default "`gene_name`" Attribute Type](#default-attribute-type)
  * [Extra Gene Names or IDs](#extra-gene-names-or-ids)
  * [Default "`exon`" Attribute](#default-exon-type)
* [Output](#Output)
 * [FeatureCounts' merged counts](#FeatureCounts'-merged-counts)
* [Troubleshooting](#Troubleshooting)
<!-- TOC END -->

## Introduction
### What's nf-core
nf-core is a community effort to collect a curated set of analysis pipelines built using Nextflow.

For facilities it provides highly automated and optimized pipelines that guaranty reproducibility of results for their users. Single users profit from portable, documented and easy to use workflows.

### What's Nextflow

Nextflow is a workflow manager. It has been developed specifically to ease the creation and execution of bioinformatics pipelines.
Whether your pipeline is a simple BLAST execution or a complex genome annotation pipeline, you can build it with Nextflow.

### What's nf-core/rnaseq

**nf-core/rnaseq** is a bioinformatics analysis pipeline used for RNA sequencing data.

The workflow processes raw data from FastQ inputs (FastQC, Trim Galore!), aligns the reads (STAR or HiSAT2), generates counts relative to genes (featureCounts, StringTie) or transcripts (Salmon, tximport) and performs extensive quality-control on the results (RSeQC, Qualimap, dupRadar, Preseq, edgeR, MultiQC).
```bash
NXF_OPTS='-Xms1g -Xmx4g'
```
## Installation
nf-core/rnaseq can run on both local/virtual environment. For the sake of system environment setup, sensitive data security and management, maintaining transparency and easy to share, we recommend using powerPlant via putty (SSH client) to install and run nf-core/rnaseq analysis.

### powerPlant usage 
Before any pipeline/workflow installation, user should read [powerPlant User Guide](https://powerplant.pfr.co.nz/guide/) carefully, important topics relate to nf-core/rnaseq installation and running on powerPlant, such as: [Storage](https://powerplant.pfr.co.nz/guide/storage), [Putty](https://powerplant.pfr.co.nz/guide/cli), [Anaconda](https://powerplant.pfr.co.nz/guide/anaconda) and [Environment Modules](https://powerplant.pfr.co.nz/guide/modules) etc.

### Installation preparation
You can create project directories under /powerplant/workspace/hra-xxx
```bash
mkdir -p nf-core
mkdir -p project_name
```
Any pipeline related contents should be installed in nf-core folder, the results/output can be saved in project_name folder. By default, the nf-core/rnaseq pipeline output saves to the results and work directory. User can type ``` --outdir /powerplant/workspace/hra-xxx/project_name ```to save results in the specific directory.

Installing and running nf-core/rnaseq on powerPlant requires virtual environment (conda/singularity/docker). Anaconda is available on powerPlant, simply type 
```bash 
module load conda 
``` 
For new user to create a new environment, using the command: 
```bash
conda create --name hraxxx python=3 
```
Then activate the environment
```bash
conda activate hraxxx
```
Alternatively, user can create a new environment with both nextflow and nf-core/tools
```bash
conda create --name hraxxx_nf-core python=3 nf-core nextflow
```
Then you can activate this environment and run the pipeline without the installation in the next two sections.

### Nextflow Installation
Install nextflow to nf-core folder
```bash
curl -fsSL get.nextflow.io | bash
```
Then add Nextflow binary to your user's PATH (make bin folder first)
```bash
mkdir -p bin
mv nextflow /powerplant/workspace/hraxxx/nf-core/bin
```
### nf-core Installation
In the same nf-core folder, you can install nf-core/tools from PYPI using pip:
```bash
pip install nf-core
```
Then you can type ```nf-core``` to check if it's successfully installed, the nf-core logo, and a list of options and commands should be displayed. 
[nf-core/tools guide](https://github.com/nf-core/tools) has more usage information. 

### nf-core/rnaseq Installation
User can download specific pipelines with the command:
```bash
$ nf-core download rnaseq
```
## Pipeline configuration & pre-running setup

A pre-built nf-core/rnaseq pipeline using malus ambrosia data (/input/genomic/plant/Malus/domestica/AGRF_CAGRF17242_CCADVANXX) is available in /powerplant/workspace/hrajaw/nf-core.
You can review the output in the results and work directory.
This pipeline can be used as a reference in the pipeline usage guide. 

### Pipeline configuration

nf-core [pipeline configuration guide](https://nf-co.re/usage/configuration) has the details of how to configure Nextflow to work on your system.

### Reference genomes

By default, the pipeline uses [iGenomes](https://github.com/nf-core/rnaseq/blob/master/conf/igenomes.config) references. To run the pipeline, you must specify which to use with the --genome flag. You can use your own reference files if they are not part of the iGenomes resource. 
Create name.config file in /nf-core-rnaseq-1.4.2/configs directory, the syntax for this .config file is as follows:
```bash
params {
  genomes {
    'Name_You_Want' {
      star    = '<path to the star index folder>'
      fasta   = '<path to the genome fasta file>' // Used if no star index given
      gtf     = '<path to the genome gtf file>'
      bed12   = '<path to the genome bed file>' // Generated from GTF if not given
    }
    // Any number of additional genomes, key is used with --genome
  }
}
```
Then modify nextflow.config in the same directory by adding ``` includeConfig("name.config") ```. 

When running the pipeline, type ``` -c /powerplant/workspace/hrajaw/nf-core-rnaseq-1.4.2/configs/nextflow.config ``` to specify the path to the config file.

And type ``` --genome Name_You_Want ``` to specify the reference genomes you just configured. 

The config files used in the malus ambrosia rnaseq pipeline are available in this repository.

### Pre-running setup

The genome fasta files often contain a long and complex string filename, because the pipeline uses the input filename as results filename, the output might be difficult to read. We can create soft-link with shorter and simplified filename before provide it to the pipeline.
By using this way, we can also easily manage the input genome fasta files.   
Create the soft-link directory under project_name folder:
```bash
mkdir -p fasta_soft-link
cd fasta_soft-link
```
Then, create the soft-link files with the command:
```bash
ln -s [file_path/file_name] [virtual_file_path/soft-link_file_name]
```
For instance, one of the soft-links used in the malus ambrosia rnaseq pipeline was generated with the command:
```bash
ln -s /input/genomic/plant/Malus/domestica/AGRF_CAGRF17242_CCADVANXX/2_ambrosiaB2_CCADVANXX_GTTTCGGA_L008_R1.fastq.gz /powerplant/workspace/hrajaw/Genome_soft_link/1_ambrosiaB1_R2.fastq.gz
```
And the soft-link files are available in /powerplant/workspace/hrajaw/nf-core/Genome_soft_link.

## Running the pipeline

Using appropriate server host to run the pipeline, see [powerPlant Architecture](https://powerplant.pfr.co.nz/guide/architecture) for details.

The typical command for running the pipeline with pair-ended data is as follows:

```bash
nextflow run nf-core/rnaseq -profile conda --reads '/soft-link dir/*_R{1,2}.fastq.gz' -c /configs/nextflow.config --genome Name_You_Want --skipBiotypeQC --outdir /project_name
```
This will launch the pipeline with the `conda` configuration profile. See below for more information about profiles.

``` --skipBiotypeQC ```
This skips the BiotypeQC step in the ```featureCounts``` process, explicitly useful when there is no available GTF/GFF with any biotype or similar information that could be used before.

Note that the pipeline will create the following files in your specified directory:

```bash
work            # Directory containing the nextflow working files
results         # Finished results (configurable, see below)
.nextflow_log   # Log file from Nextflow
# Other nextflow hidden files, eg. history of pipeline runs and old logs.
```

### Reproducibility

It's a good idea to specify a pipeline version when running the pipeline on your data. This ensures that a specific version of the pipeline code and software are used when you run your pipeline. If you keep using the same tag, you'll be running the same version of the pipeline, even if there have been changes to the code since.

First, go to the [nf-core/rnaseq releases page](https://github.com/nf-core/rnaseq/releases) and find the latest version number - numeric only (eg. `1.3.1`). Then specify this when running the pipeline with `-r` (one hyphen) - eg. `-r 1.3.1`.

This version number will be logged in reports when you run the pipeline, so that you'll know what you used when you look back in the future.

## Main arguments

### `-profile`

Use this parameter to choose a configuration profile. Profiles can give configuration presets for different compute environments. Note that multiple profiles can be loaded, for example: `-profile docker` - the order of arguments is important!

If `-profile` is not specified at all the pipeline will be run locally and expects all software to be installed and available on the `PATH`.

* `awsbatch`
  * A generic configuration profile to be used with AWS Batch.
* `conda`
  * A generic configuration profile to be used with [conda](https://conda.io/docs/)
  * Pulls most software from [Bioconda](https://bioconda.github.io/)
* `docker`
  * A generic configuration profile to be used with [Docker](http://docker.com/)
  * Pulls software from dockerhub: [`nfcore/rnaseq`](http://hub.docker.com/r/nfcore/rnaseq/)
* `singularity`
  * A generic configuration profile to be used with [Singularity](http://singularity.lbl.gov/)
  * Pulls software from DockerHub: [`nfcore/rnaseq`](http://hub.docker.com/r/nfcore/rnaseq/)
* `test`
  * A profile with a complete configuration for automated testing
  * Includes links to test data so needs no other parameters

### `--reads`

Use this to specify the location of your input FastQ files. For example:

```bash
--reads 'path/to/data/sample_*_{1,2}.fastq'
```

Please note the following requirements:

1. The path must be enclosed in quotes
2. The path must have at least one `*` wildcard character
3. When using the pipeline with paired end data, the path must use `{1,2}` notation to specify read pairs.

If left unspecified, a default pattern is used: `data/*{1,2}.fastq.gz`

### `--singleEnd`

By default, the pipeline expects paired-end data. If you have single-end data, you need to specify `--singleEnd` on the command line when you launch the pipeline. A normal glob pattern, enclosed in quotation marks, can then be used for `--reads`. For example:

```bash
--singleEnd --reads '*.fastq'
```

It is not possible to run a mixture of single-end and paired-end files in one run.

## FeatureCounts Extra Gene Names

### Default "`gene_name`" Attribute Type

By default, the pipeline uses `gene_name` as the default gene identifier group. In case you need to adjust this, specify using the option `--fc_group_features` to use a different category present in your provided GTF file. Please also take care to use a suitable attribute to categorize the `biotype` of the selected features in your GTF then, using the option `--fc_group_features_type` (default: `gene_biotype`).

### Extra Gene Names or IDs

By default, the pipeline uses `gene_names` as additional gene identifiers apart from ENSEMBL identifiers in the pipeline.
This behaviour can be modified by specifying `--fc_extra_attributes` when running the pipeline, which is passed on to featureCounts as an `--extraAttributes` parameter.
See the user guide of the [Subread package here](http://bioinf.wehi.edu.au/subread-package/SubreadUsersGuide.pdf).
Note that you can also specify more than one desired value, separated by a comma:
`--fc_extra_attributes gene_id,...`

### Default "`exon`" Type

By default, the pipeline uses `exon` as the default to assign reads. In case you need to adjust this, specify using the option `--fc_count_type` to use a different category present in your provided GTF file (3rd column). For example, for nuclear RNA-seq, one could count reads in introns in addition to exons using `--fc_count_type transcript`.

## Output
By default, the nf-core/rnaseq pipeline does not save large intermediate files to the
results directory. This is to try to conserve disk space.

These files can be found in the pipeline `work` directory if needed.

### FeatureCounts' merged counts

The pipeline's merged counts function might not work on multiple pair-ended data. 
A script is provided to solve this issue, you can run this script in the same directory with the gene_counts files.
The syntax for this python script is as follows: 
```bash
import pandas as pd
file1 = pd.read_csv('[gene_counts output filename]Aligned.sortedByCoord.out_gene.featureCounts.txt', sep="\t", skiprows=1,usecols =['Geneid','gene_counts_output_ filenameAligned.sortedByCoord.out.bam'])
...                                        
...
...
file_n = pd.read_csv('[gene_counts output filename]Aligned.sortedByCoord.out_gene.featureCounts.txt', sep="\t", skiprows=1,usecols =['gene_counts_output_ filenameAligned.sortedByCoord.out.bam'])
res = pd.concat([file1,...,file_n],axis=1, join='outer').sort_index()
res.to_csv('Name_You_Want.txt', index=False, sep=' ')
```
This will generate a merged gene counts file in the same directory. 

The python merge script used in malus ambrosia rnaseq pipeline is available in this repository.

## Troubleshooting

You can visit the official [nf-core](https://github.com/nf-core/tools) and [nf-core/rnaseq](https://github.com/nf-core/rnaseq/tree/master/docs) user guide for more usage details.

If you have issues that are not mentioned in [Troubleshooting](https://nf-co.re/usage/troubleshooting) or the official documentations, feel free to contact nf-core's dev team via the [Slack](https://nf-co.re/join/slack) channel or me (jack.wang@plantandfood.co.nz).


