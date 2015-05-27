#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
import sys, re

f = open(sys.argv[1])

#for skip in range(5):
#    f.next()
for i in f:
    line = i.strip().split('\t')
    if line[2] == 'exon':
         #geneName = re.search('ID=[A-Za-z0-9]*.\d*.\d*', line[8])
         #print geneName.group(0)
         newItem = line[8].split(';')[-1]
         #secondBit = line[8].split('=')[-1]+'-Protein;'
         #firstBit = line[8].split(';')[-1]
         #newItem = firstBit+','+secondBit
         line.pop()
         line.append(newItem)
    print '\t'.join(line)
    #if len(i.strip().split("\t")) != 9:
    #    print i
    ##----------------------------------------------------------------------
    ## Joe's hack
    ##----------------------------------------------------------------------
    #line = i.split("\t")
    #itemTwo = line[1]
    #columnTwo = line[1].split()
    #firstAttr = columnTwo[0].replace("/", "_")
    #secondAttr = columnTwo[1]
    #thirdAttr = ''.join(columnTwo[-2].split("_"))
    #fourthAttr = columnTwo[-1].strip("()")
    #modifiedColumnTwo = '_'.join([firstAttr, secondAttr, thirdAttr, fourthAttr])
    #line.remove(itemTwo)
    #line.insert(1, modifiedColumnTwo)
    #print '\t'.join(line).strip()
    ##----------------------------------------------------------------------

#    #----------------------------------------------------------------------
#    line = i.split("\t")
#    attrs = line[8].strip().split(";")
#    typeAttr = attrs[4]
#    newType = typeAttr.replace('gene_biotype', 'transcript_type')
#    attrs.insert(2, newType)
#    newAttrs = ';'.join(attrs)
#    #print i.replace(line[8], newAttrs).strip()
#    print '\t'.join(line).strip()
    #----------------------------------------------------------------------
    #geneCheck = line[2]
    #if geneCheck == 'gene':
    #    #print line
    #    columnNine = line[8]
    #    attrs = columnNine.split(";")
    #    geneIDAttr = attrs[0]
    #    geneBiotypeAttr = attrs[-2]

    #    transcriptIDAttr = geneIDAttr.replace('gene_id', ' transcript_id')
    #    transcriptBiotypeAttr = geneBiotypeAttr.replace('gene_biotype', 'transcript_biotype')

    #    attrs.insert(1, transcriptIDAttr)
    #    attrs.insert(-2, transcriptBiotypeAttr)
    #    newAttrs = ';'.join(attrs)
    #    line.pop()
    #    line.insert(-1, newAttrs)
    #    line.pop()
    #    print "\t".join(line).strip()
    #else:
    #    print "\t".join(line).strip()
