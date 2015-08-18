#!/bin/bash

#------------------------------
# Serine #MonashFlavour
#------------------------------

#------------------------------
# Help string
#------------------------------
# In BASH $@ represents all the arguments in the command line
if [[ -z "$@" ]];then
  echo
  echo Usage: changePreFix.bash \<directory with fastq files\> \<namesPreFix.txt\>
  echo
  echo This script creates symlink with changed files prePix
  echo e.g A_sampleFile.fastq.gz -\> newPreFix_sampleFile.fastq.gz
  echo
  echo Make a file with two columns, tab delimited, where:
  echo - column 1 = current file preFix 
  echo - column 2 = new file preFix 
  echo
  exit 1
fi

#------------------------------
# Body
#------------------------------
# First argument is the directory with fastq files
fqFiles=`find $1 -name '*.gz' -type f`
# Loop over fastq files
for i in $fqFiles;do
  # get the actual file 
  rootName=$(basename $i)
  # for each file read lines from namesPreFix.txt file
  while read -r line || [[ -n $line ]];do
    eval string=($line)
    check=${string[0]}
    name=${string[1]}
    # chek if file starts with column one item
    if [[ $rootName == $check* ]];then
      # if it does substitute old preFix with new preFix from column two
      fileName="${rootName/$check/$name}"
      # make symlink in a current directory
      ln -s $i $fileName
      #echo $fileName $check $name
    fi
    done < "$2"
done

#------------------------------
# End
#------------------------------
