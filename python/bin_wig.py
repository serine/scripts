#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

"""

This scrtip takes .bam file as its input. (bear in mind that pysam requires an index file in the same directory)
It outputs flat text file, space separated, with three columns, Name Bin number Bin number. The bin size can be changed
The default bin size is 50

"""

import sys, re, pysam
from math import floor

start = ''
store = []
last_pos = None
new_pos = None
count = 0
strand = ''

samfile = pysam.AlignmentFile(sys.argv[1], 'rb')

for i in samfile.fetch():

    if i.has_tag('AN'):
        if i.is_reverse:
            start = i.pos
            end = start
            ref_id = i.reference_id
            name = samfile.getrname(ref_id)
            strand = '-'
            
            v = floor(start/50) * 50
            if count > 0:
                if v in store:
                    count += 1
                    store.pop()
                    store.append(count)
                else:
                    print ' '.join([store[0], str(int(store[2])), str(int(store[2])), strand])
                    count = 0
            else:
                count += 1
                store = [name, start, v, count]

        else: 
            start = i.reference_end
            end = start
            ref_id = i.reference_id
            name = samfile.getrname(ref_id)
            strand = '+'
            
            v = floor(start/50) * 50
            if count > 0:
                if v in store:
                    count += 1
                    store.pop()
                    store.append(count)
                else:
                    print ' '.join([store[0], str(int(store[2])), str(int(store[2])), strand])
                    count = 0
            else:
                count += 1
                store = [name, start, v, count]
