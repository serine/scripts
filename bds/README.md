# This is documentation for `rnas-pipe` BDS script located in this sub-repository

I have used BDS to write a pipeline for RNA-seq data primary manipulation. 
Once you get your raw `FASTQ` files from the sequencing facility you need to
make some quick sense. The things you probably would like to know straight away
include:

 - How many reads from my RNA-seq sample have mapped to the reference genome?
 - How many of those reads have mapped ambiguously?
 - How many reads fallen on the feature i.e mapped directly onto the gene?

The `rnas-pipe` takes care of all of these problems. There are three main sections at this stage

 1. Reads alignment. Currently it is set to `STAR` with predefined `STAR` input parameters
    It is rather stringent at this stage and only through manual intervention one can change the input
    parameters inside the source code. Feel free to `git clone` and edit source to your needs. 
    There are the parameters `STAR` set up to run with in BDS by default.

    ```
    STAR --runThreadN 26 \
         --genomeDir $genomeIndex \
         --outSAMtype BAM Unsorted \
         --outSAMattrRGline ID:$laneNumber CN:AGRF DS:RNA-seq PL:ILLUMINA PM:MiSeq SM:$uniqueName \
         --outSAMunmapped Within \
         --readFilesCommand zcat \
         --readFilesIn $read1 $read2 \
         --outFileNamePrefix $preFix
    ```
  2. Several `picard` pre-processing steps for `RNA-SeQC` run later. `picard` produces, sorted, reordered bam files
     with marked duplicates. This is prerequisite for `RNA-SeQC` run

  3. `htseq-count` that count how many reads mapped one genes 
