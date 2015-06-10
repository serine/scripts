#!/bin/bash

for i in chr2Bams/*.bam;
do
  NAME=$(basename ${i%.*}).vcf
  samtools mpileup -g -f ~/ref-files/landsberg_erecta/ler_0.v7.fa chr2Bams/$i | bcftools call -c -v - > calledVCF/$NAME
done
