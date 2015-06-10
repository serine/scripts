#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

import sys, re

f = open(sys.argv[1])

listOfFeatures = ["Gene", "Transcript", "five_prime_UTR", "three_prime_UTR", "CDS", "exon"]
#for p in range(15):
#   f.next()
for i in f:
    line = i.strip()
    if not line.startswith("#"):
        items = line.split()
        #print items[7]
        m = re.search("CDS", items[7])
        if m:
            tt = m.string.split(";")[0]
            #re.search("CDS", tt)
            #print tt.split(":")
            print tt.split(":")[1]
