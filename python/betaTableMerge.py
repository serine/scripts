#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

import sys, os, csv

listOfFiles = []
#testList = [["this", "3", "lst", "one"],r  
#           ["this", "3", "lst", "two"],
#           ["this", "3", "lst", "three"]
#          ]

#testList = [[1,2,3], [4,5,6], [7,8,9]]
for root, dirs, files in os.walk(sys.argv[1]):
    if dirs:
        if "strandedReverse" in dirs:
            test = dirs[dirs.index("strandedReverse")]
            testDir = os.path.join(root, test)
            if testDir:
                for i in os.listdir(testDir):
                    if i != ".dir_bash_history":
                        listOfFiles.append(os.path.join(testDir, i))
output = open("htseq-cout-table.txt", "w")

column = []
columns = []
nameColumn = []

for textFile in listOfFiles:
    f = open(textFile)
    
    for line in f:
        tt = str(f)
        tmpName = tt.split("/")[-1]

        if tmpName.startswith("cf"):
            tmpRoot = tmpName.split("_")
            tmp1 = tmpRoot.pop()
            tmp2 = tmpRoot.pop()
            rootName  = ''.join(tmpRoot)
            theName = str(rootName.split("-")[1])
            #print theName

        else:
            tmpRoot = tmpName.split("_")
            theName = str(tmpRoot[0])
            #print theName

#       print tt.split()[2]
#     
        if not line.startswith("__"):

            info = line.strip().split()[-1]
            name = line.strip().split()[0]
            if theName not in column:
                column.append(theName)
            column.append(info)

        if len(nameColumn) < 65218:
            if not nameColumn:
                nameColumn.append('Ensembl gene names')
            nameColumn.append(name)


    if nameColumn not in columns:
        
        columns.append(nameColumn)

    columns.append(column)
    column = []
#print len(columns)#
for betterName in zip(*columns):
    #print len(betterName)
    #print betterName
    #print '\t'.join(betterName)
    output.write('\t'.join(betterName)+'\n')
