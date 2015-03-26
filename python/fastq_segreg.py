#! /usr/bin/env python

#This is a segregation tool for fastq files with paired-end reads. It take one file and segregates it into two individual files with corresponding names 

import sys

#open a file given as a first argument
fastq_in = open(sys.argv[1])

#create two files, one for each read type 
fastq1 = open('read1.fq', 'w')
fastq2 = open('read2.fq', 'w')

reads1 = []
reads2 = []

line = True
#while the condition is true execute the code in the while loop
while line:
    lines = []
    #get four rows at a time and append them into lines list
    for i in range(4):
        line = fastq_in.readline().strip()
        if line: 
            lines.append(line)
    #join items in the lines list. The read object represents a single read
    read = '\t'.join(lines)
    
    #check if a read belongs to a read1 family. if so put it into reads1 list
    if read.split('\t')[0].endswith('1'):
        reads1.append(read.split())
    #otherwise it must be a read2 famly member, put it into reads2 list
    else:
        reads2.append(read.split())
#write both list to the appropriate files
fastq1.writelines(['%s\n' % item for item in [item for i in reads1 for item in i]])
fastq2.writelines(['%s\n' % item for item in [item for i in reads2 for item in i]])
