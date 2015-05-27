#! /bin/bash

#TMP=((one 1) (two 2) (three 3))
#CHECK="R1"

#for i in "$@" 
#do
#  ln -s $i $(basename "${i/%_001.fastq.gz/.fastq.gz}")
#  #if [[ $i =~ $CHECK ]]; then
#  #  echo $i
#  #fi
##  #--------------------------------------------------
##  # good script
##  #--------------------------------------------------
##  if [ "${i/$CHECK}" != "$i" ]; then
##    TEST="${i/%R1_001.fastq.gz/L001_R1.fastq.gz}"
##    ln -s $i $(basename $TEST)
##  else
##    TEST="${i/%R2_001.fastq.gz/L001_R2.fastq.gz}"
##    ln -s $i $(basename $TEST)
##  #--------------------------------------------------
##  fi
#done
#while read line
#do
#  for i in "$@"
#  do
#    echo $(basename $i) $line
#  #if [[ "$i" =~ $REGEX ]]; then
#  #  echo $i $line
#  #fi
#  done
#done < $1
#echo ${CHECK[*]}
#
#for filename in $@; do
#  #echo $filename
#  for item in ${CHECK[*]}; do
#    #echo $item $(basename $filename)
#    if [[ $item =~ $(basename $filename) ]]; then
#      echo $item $(basename $filename)
#    fi
#  done
#done
CHECK=(GLP1-7-low_LB01_S1
       GLP1-7-low_LB02_S2
       GLP1-7-low_LB03_S3
       GLP1-7-high_LB04_S4
       GLP1-7-high_LB05_S5
       GLP1-7-high_LB06_S6
       Exendin-7-low_LB07_S7
       Exendin-7-low_LB08_S8
       Exendin-7-low_LB09_S9
       Exendin-7-high_LB10_S10
       Exendin-7-high_LB11_S11
       Exendin-7-high_LB12_S12
       Glucose-low_LB13_S13
       Glucose-low_LB14_S14
       Glucose-low_LB15_S15
       Glucose-high_LB16_S16
       Glucose-high_LB17_S17
       Glucose-high_LB18_S18)


REGEX='(LB[0-9]{2}_S[0-9])'
for item in ${CHECK[*]}; do
  for filename in $@; do 
    if [[ "$item" =~ $REGEX ]]; then
      if [[ "$(basename $filename)" =~ $BASH_REMATCH ]]; then
        STR=$(basename $filename)
        CHECKMATE=$(perl -e '($a,$b) = @ARGV; $a=~s/_001//; $b=~s/_LB.*//; print "${b}_$a\n"' $STR $item)
        ln -s $filename $CHECKMATE
      #echo "$item$STR" | sed -e 's/LB.._S.{1,2}L/L/'
      fi
    fi
  done
done
