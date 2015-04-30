#! /bin/bash

CHECK="R1"

for i in "$@" 
do
  #echo $i
  #if [[ $i =~ $CHECK ]]; then
  #  echo $i
  #fi
  if [ "${i/$CHECK}" != "$i" ]; then
    TEST="${i/%R1_001.fastq.gz/L001_R1.fastq.gz}"
    #ln -s $i $TEST
    ln -s $i $(basename $TEST)
  else
    TEST="${i/%R2_001.fastq.gz/L001_R2.fastq.gz}"
    ln -s $i $(basename $TEST)
    #ln -s $i $TEST
  fi
done
