#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

import sys, os

listOfFiles = []

for root, dirs, files in os.walk(sys.argv[1]):
        if dirs:
                if "strandedReverse" in dirs:
                        test = dirs[dirs.index("strandedReverse")]
                        testDir = os.path.join(root, test)
                        if testDir:
                                for i in os.listdir(testDir):
                                        listOfFiles.append(os.path.join(testDir, i))

output = open("theTable.txt", "w")
columns = []
tempList = []

for i in listOfFiles:
        f = open(i)
        for line in f:
                if line.startswith("__"):
                        info = line.strip().split("__")[-1].split()
                        name = i.split("/")[-1].split("Aligned")[0]
                        tempList.append(info[1])

                        if info[0] not in columns:
                                columns.append(info[0])
                                
                        if name not in tempList:
                                tempList.insert(0, name)

        #print (",").join(tempList)
        
        output.write(("\t").join(tempList)+"\n")
        tempList = []
#print columns
