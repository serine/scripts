#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

import argparse, sys

##creat optional arguments using argparse module
#parser = argparse.ArgumentParser()
#parser.add_argument('-i', '--infile', nargs=1, type=argparse.FileType('r'))
#parser.add_argument('-o2', '--outfile_two', nargs='?', type=argparse.FileType('w'))
#args = parser.parse_args()
##take the first item from in infile list 
#fastq_in = args.infile[0]

f = open (sys.argv[1])

testDict = {}

for skip in range(0,5):
    f.next()

for i in f:
    line = i.strip().split("\t")
    #testList = i.strip().split("\t")[8]
    geneTest = line[2] 
    if geneTest == 'gene':
        info = line[8].split(";")
         
        gene_id = info[4].split()[1].strip('"')
        ensemble_id = info[0].split()[1].strip('"')
        biotype = info[2].split()[1].strip('"')

        testDict[ensemble_id]=[ensemble_id, gene_id, biotype]

for key, value in testDict.items():
    print value
         #print line
    #    if 'transcript_id' in testList:
    #        ids = testList.split(";")
    #        print geneTest, ids[0], ids[1]
    #    #   print i.split()
    #if i.split()[-1] == "'rRNA'":
    #biotype = i.strip().split("\t")[-1].split(";")[4]
    #if 'gene_biotype' in biotype:
    #    testWord = biotype.split()[1].strip('"')
    #    if 'rRNA' in testWord:
    #        print i.strip()
