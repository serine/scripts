#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

import sys, re

geneHash = {}
bootstrap = 'ID=%s;Note=%s;Name=%s'
# pseudogenic_exon

toInsert = ['miRNA', 
            'other_RNA',
            'protein_coding_gene',
            'rRNA',
            'snoRNA',
            'tRNA',
           ]

toCheck = ['CDS',
           'exon',
           'five_prime_UTR',
           'gene',
           'miRNA',
           'mRNA',
           'ncRNA',
           'protein',
           'pseudogene',
           'pseudogenic_transcript',
           'rRNA',
           'snoRNA',
           'three_prime_UTR',
           'transposable_element_gene',
           'tRNA',
          ]
features = []
gene = None

for i in open(sys.argv[1]):
    line = i.split()
    if line[2].strip() == 'gene':
        if features:
            #print gene
            print features[0]
            #print '----------'

        features = []
        gene = line
    else:
        features.append(i.strip())
#for i in open(sys.argv[1]):
#   line = i.strip().split("\t")
#   m = re.search(':([A-Z0-9]+)', line[8])
#   key = m.group(1) 
#   #value = '\t'.join([line[0], line[-1]])
#   value = i
#
#   if key not in geneHash:
#       geneHash[key] = []
#
#   geneHash[key].append(value)
#   #print key, value
#   #print line[-1]
#
##for key, value in geneHash.items(): #.values():
##  print key, value
#for key, value in geneHash.items():
#   for i in value:
#       m = re.search('mRNA', i)
#       if m:
#           print m.group(0)
#       #m = re.search('mRNA', value)
#   #print m.group(0)
#   break
    #for i in value:
    #   print i.strip()
    #   line = i.split("\t")
    #   if line[0] in toCheck:
    #       #getIndex = check.index(i)
    #       if i.startswith(i):
    #           print bootstrap % (key, 'protein_coding_gene', key)
    #   print line[0]
    #break
