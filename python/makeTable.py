#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

import argparse, sys, os, csv
from collections import defaultdict

#creat optional arguments using argparse module
parser = argparse.ArgumentParser(description="learnign to use argparse")

parser.add_argument('--rootDir',  default=os.getcwd(), help="specify root directory")
parser.add_argument('--fileDir', nargs=1, default=argparse.SUPPRESS, help="specify files directory")
parser.add_argument('--gtfFile', help="specify path to the gtf file")
#parser.print_help()

args = parser.parse_args()
rootDir = args.rootDir
fileDir = args.fileDir[0]
gtfFile = args.gtfFile

#----------------------------------------------------------------------
# This section traverses the root directory and looks for the 
# strandedreverse directories that hold htseq-count report files
# It then appends all files from those stranded reverse directories
# to one list listOfFiles
#----------------------------------------------------------------------

f = open(gtfFile)

testDict = {}

for skip in range(5):
     f.next()
for i in f:
     line = i.strip().split("\t")
     geneTest = line[2] 
     if geneTest == "gene":
         info = line[8].split(";")
          
         gene_id = info[4].split()[1].strip('"')
         ensemble_id = info[0].split()[1].strip('"')
         biotype = info[2].split()[1].strip('"')

         testDict[ensemble_id]=[ensemble_id, gene_id, biotype]

#for key, value in testDict.items():
#    print value

def getListOfFiles(rootDir, fileDir):
    """
    This function loop over a root directory and searches for 
    subdirectories under the root. Sub-directory is specified by
    --fileDir.  The function return a list of files from sub-directory,
    i.e from all directories under the root that match --fileDir input.
    """
    
    listOfFiles = []

    for root, dirs, files in os.walk(rootDir):
        if dirs:
            if fileDir in dirs:
                test = dirs[dirs.index(fileDir)]
                testDir = os.path.join(root, test)
                if testDir:
                    for i in os.listdir(testDir):
                        if i != ".dir_bash_history":
                            listOfFiles.append(os.path.join(testDir, i))
    return listOfFiles

listOfFiles = getListOfFiles(rootDir, fileDir)

dataDict = defaultdict(list)
dataList = []
column = []
rightOrder = []

for textFile in listOfFiles:
    """
    Here I'm looping over list of files
    - open each file
    - exctract information from each file
    - save extracted information
    - move on to the next file
    """
    # open a file
    f = open(textFile)
    # loop over each line in the file
    for line in f:

        #-------------------------------------------------------
        # This section is specifit for columns name formating
        #-------------------------------------------------------

        fileAsStr = str(f)
        tmpName = fileAsStr.split("/")[-1]
        
        if tmpName.startswith("cf"):

            tmpRoot = tmpName.split("_")
            tmp1 = tmpRoot.pop()
            tmp2 = tmpRoot.pop()
            rootName  = ''.join(tmpRoot)
            sampleId = str(rootName.split("-")[1])

        else:

            tmpRoot = tmpName.split("_")
            sampleId = str(tmpRoot[0])
        #-------------------------------------------------------

        if not line.startswith("__"):
            # get values from the file
            dataValue = line.strip().split()[-1]
            # get name from the file
            EnsemblName = line.strip().split()[0]
            
            if not column:
                column.append('Ensembl ID')
                column.append('Biotype')
                column.append('Gene name')

            if len(rightOrder) < 65217:
                rightOrder.append(EnsemblName)

            if len(dataDict) < 65217:
                dataList = testDict.get(EnsemblName)
                dataList.append(dataValue)
                dataDict[EnsemblName] = dataList
            else:
                dataDict[EnsemblName].append(dataValue)

            if sampleId not in column:
                column.append(sampleId)

print '\t'.join(column)
for order in rightOrder:
    print '\t'.join(dataDict.get(order))
