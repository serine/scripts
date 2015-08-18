#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

# (+_+)

import argparse, sys, os, re, gffutils

#creat optional arguments using argparse module
parser = argparse.ArgumentParser(description="Use this script to make one table\
                                              with all the samples read counts.\
                                              This is primary for Degust\
                                              visualisation and DE analysis")

parser.add_argument('--headerSkip', default=2, help="specify number of line to skip in the count file, default assumes featureCount, which has two header lines")
parser.add_argument('--fileDir', nargs=1, default=argparse.SUPPRESS, help="specify files directory")
parser.add_argument('--databaseFile', nargs=1, default=argparse.SUPPRESS, help="specify files directory")

if len(sys.argv)==1:
        parser.print_help()
        sys.exit(1)

args = parser.parse_args()
headerSkip = int(args.headerSkip)
fileDir = args.fileDir[0]
databaseFile = args.databaseFile[0]

db = gffutils.FeatureDB(databaseFile, keep_order=True)
features = db.all_features()

listOfFiles = os.listdir(fileDir)

dataDict = {}
dataList = []
column = []
rightOrder = []
first =True
header = False
#TODO need to check if header is a string
#TODO if string is a number then convert it to a string 
#TODO e.f 2dK01 == Twodko1 just because for downstream analysis files can't statrt with a digit
for textFile in listOfFiles:
    if textFile.endswith("txt"):
        f = open(os.path.join(fileDir, textFile))
        # skip the header
        # featureCounts only has two lines of header
        for i in range(headerSkip):
            f.next()
            #-------------------------------------------------------
            # This section is specific for columns name formating
            #-------------------------------------------------------
            preName = textFile.split('_')
            fileName = preName[0]

        for line in f:
            c = line.strip().split()
            geneId = c[0]
            if geneId not in dataDict:
                dataDict[geneId] = [(c[6], fileName)]
            else:
               dataDict[geneId].append((c[6], fileName))

for line in features:
    if line.featuretype == 'gene':
        geneId = line.id
        geneName = line.attributes['gene_name'].pop()
        geneType = line.attributes['gene_biotype'].pop()
        v = dataDict[geneId]
        dataItems = '\t'.join([f[0] for f in v])
        if not header:
            header = '\t'.join([f[1] for f in v])
            print '\t'.join(('Ensembl ID', 'Gene Name', 'Biotype', header))
        print '\t'.join((geneId, geneName, geneType, dataItems))
