#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

# (+_+)

import argparse, sys, os, re
from collections import defaultdict

#creat optional arguments using argparse module
parser = argparse.ArgumentParser(description="Use this script to make one table\
                                              with all the samples read counts.\
                                              This is primary for Degust\
                                              visualisation and DE analysis")

parser.add_argument('--lines2Skip', default=5, help="specify number of line to skip in the gtf file, default is 0")
parser.add_argument('--fileDir', nargs=1, default=argparse.SUPPRESS, help="specify files directory")
parser.add_argument('--gtfFile', nargs=1, help="specify path to the gtf file")

if len(sys.argv)==1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()
lines2Skip = args.lines2Skip
fileDir = args.fileDir[0]
gtfFile = args.gtfFile[0]

#----------------------------------------------------------------------
# This section traverses the root directory and looks for the 
# strandedreverse directories that hold htseq-count report files
# It then appends all files from those stranded reverse directories
# to one list listOfFiles
#----------------------------------------------------------------------

f = open(gtfFile)

testDict = {}

for skip in range(int(lines2Skip)):
     f.next()
for i in f:
    line = i.strip().split("\t")
    geneTest = line[2] 
    if geneTest == "exon":
        #geneId = re.search('(gene_id\W+)([A-Z0-9]+)', line[8])
        #geneName = re.search('(gene_name\W+)([A-Za-z0-9]+|gene_name\W+[A-Za-z0-9]+.\d+)', line[8])
        #geneType = re.search('(gene_biotype\W+)([A-Za-z]+)', line[8])

        geneId = re.search('(gene_id\W+)([A-Z0-9]+)', line[8])
        geneName = re.search('(gene_name\W+)([A-Za-z0-9]+)', line[8])
        geneType = re.search('(gene_biotype\W+)([A-Za-z]+|[0-9A-z]+)', line[8])

        if geneName:
            if geneId.group(2) not in testDict:
                testDict[geneId.group(2)]=[geneId.group(2), geneName.group(2), geneType.group(2)]
        else:
            if geneId.group(2) not in testDict:
                testDict[geneId.group(2)]=[geneId.group(2), geneId.group(2), geneType.group(2)]

#for key, value in testDict.items():
#   print value

listOfFiles = os.listdir(fileDir)

#dataDict = defaultdict(list)
dataDict = {}
dataList = []
column = []
rightOrder = []
first =True

for textFile in listOfFiles:
    if textFile.endswith("txt"):
        f = open(os.path.join(fileDir, textFile))
        for line in f:
            #-------------------------------------------------------
            # This section is specific for columns name formating
            #-------------------------------------------------------
            #m = re.search('(_LB[0-9]{2})_(S[0-9]+.txt)', textFile)
            m = re.search('_(S[0-9]+.txt)', textFile)
            sampleId = textFile.replace(m.group(0), m.group(1))
            # This part is for featureCount
            if line.startswith("E"):
                 splitLine = line.strip().split("\t")
                 EnsemblName = splitLine[0]
                 dataValue = splitLine[-1]

                 if not column:
                     column.append('Ensembl ID')
                     column.append('Gene name')
                     column.append('Biotype')

                 if first:
                     rightOrder.append(EnsemblName)

                 if EnsemblName not in dataDict:
                     dataList = testDict.get(EnsemblName)
                     dataDict[EnsemblName] = dataList

                 dataDict[EnsemblName].append(dataValue)

                 if sampleId not in column:
                     column.append(sampleId)
        first=False
print '\t'.join(column)
for order in rightOrder:
    print '\t'.join(dataDict.get(order))
