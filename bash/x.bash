#!/bin/bash

#------------------------------
# Body
#------------------------------
fqFiles=`ls -1 $1*.gz`
CHECK='R1'

for i in $fqFiles; do
  #baseName=$(basename $i)
  baseName=$i
  if [[ $baseName =~ $CHECK ]]; then
    PAIR="${baseName/%R1_001.fastq.gz/R2_001.fastq.gz}"
    dirName=$(basename "${PAIR%%_*}")
    #echo $dirName
    spades.py --threads 29 --memory 125 -o $dirName --cov-cutoff 30 -1 $baseName -2 $PAIR 
  fi
done

# First argument is the directory with fastq files
## Loop over fastq files
#for i in $fqFiles;do
#  # get the actual file 
#  rootName=$(basename $i)
#  # for each file read lines from namesPreFix.txt file
#  while read -r line || [[ -n $line ]];do
#    #check=${line:0:1}
#    #name=${line:2}
#    eval string=($line)
#    check=${string[0]}
#    name=${string[1]}
#    #echo $check
#    # chek if file starts with column one item
#    if [[ $rootName == $check* ]];then
#      # if it does substitute old preFix with new preFix from column two
#      fileName="${rootName/$check/$name}"
#      # make symlink in a current directory
#      ln -s $i $fileName
#      #echo $fileName
#    fi
#    done < "$2"
#done
#
##------------------------------
## End
##------------------------------
