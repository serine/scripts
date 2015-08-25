#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

import pysam, sys

samFile = pysam.AlignmentFile(sys.argv[1], 'rb')

#print dir(samFile)

for i in samFile:
    print dir(i)
    print i.qname, i.query_name
    break
