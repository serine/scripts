#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

import sys, os, directories

columns = []
tempList = []

columnNames = ["Sample Name", "No Feature", "Ambigious", "Too Low aQual", "Not Aligned", "Alignment Not Unique"]

print "\t".join(columnNames)

for i in directories.getListOfFiles(sys.argv[1], "strandedReverse"):
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
    
    print ("\t").join(tempList)
    tempList = []
