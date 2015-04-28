#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

#----------------------------------------------------------------------------------------------------
# script traverses root directory and searchers for all the files in the specified
# sub-directories that meat the searchFor requirement
# searchFor is a regular expression search. That is searching for literal match and
# returns the string that had been matched
#----------------------------------------------------------------------------------------------------

import argparse, os, sys, shutil, directories, re

#------------------------------
# print help if no arguments
# passed in
#------------------------------

try:
    #creat optional arguments using argparse module
    parser = argparse.ArgumentParser(description="learnign to use argparse")
    
    parser.add_argument('--rootDir', default=os.getcwd(), help="specify root directory")
    parser.add_argument('--fileDir', nargs=1, help="specify sub-directory with files of interest")
    parser.add_argument('--newDir', default="newPyDir", help="specify name of the new directory")
    parser.add_argument('--searchFor', help="specify unique feature to search upone")
    
    args = parser.parse_args()
    rootDir = args.rootDir
    fileDir = args.fileDir[0]
    newDir = args.newDir
    searchFor = args.searchFor
except:
    parser.print_help()

if not os.path.isdir(newDir):
    os.makedirs(newDir)

for i in directories.getListOfFiles(rootDir, fileDir):
    m = re.search(searchFor, i)
    if m:
        shutil.copy(m.string, newDir)
