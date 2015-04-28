#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

#----------------------------------------------------------------------
#
# This is a custom scritp and that make tab deliminated table for
# RNAseQC run. 
#
#----------------------------------------------------------------------
import argparse, sys, os, csv
from collections import defaultdict

def checkInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False
#creat optional arguments using argparse module
parser = argparse.ArgumentParser(description="learnign to use argparse")

parser.add_argument('--infoTable', help="specify root directory")
parser.add_argument('--filesDir', help="specify files directory")

args = parser.parse_args()
infoTable = args.infoTable
filesDir = args.filesDir

samplesNotes = {}

for i in open(infoTable):
    line = i.strip().split("\t")
    if line[0] != "Sample ID":
        name = line[0]+"|"+line[4]
        notes = line[1]+"|"+line[3]+"|"+line[2]
        key = name.split("|")[0]
        samplesNotes[key]=((name, notes))

for item in os.listdir(filesDir):
    if item != ".dir_bash_history":
        if item.endswith(".bam"):
            if item.startswith("cf"):
                tmp = item.split("_")[0].split("-")
                if checkInt(tmp[1]):
                    name = '-'.join(tmp)
                    tt = samplesNotes.get(name)
                    print "\t".join((tt[0], item, tt[1]))
                else:
                    name = ''.join(item.split("C3PWNACXX")[0].split("_"))
                    tt = samplesNotes.get(name)
                    print "\t".join((tt[0], item, tt[1]))
            else:
                name = item.split("_")[0]
                tt = samplesNotes.get(name)
                print "\t".join((tt[0], item, tt[1]))
