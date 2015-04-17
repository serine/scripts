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
                    listOfFiles.append(os.path.join(testDir, i))

output = open("testMerge.txt", "w")

column = []
columns = []
nameColumn = []

for textFile in listOfFiles:
    f = open(textFile)
    for line in f:
      
        if not line.startswith("__"):

            info = line.strip().split()[-1]
            name = line.strip().split()[0]
            column.append(info)

        if len(nameColumn) < 65217:
            nameColumn.append(name)


    if nameColumn not in columns:
        columns.append(nameColumn)

    columns.append(column)
    column = []

for textFile in zip(*columns):
    #print textFile
    #print '\t'.join(textFile)
    output.write('\t'.join(textFile)+'\n')
