#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

"""
script that takes as input a .bam file, parsers it and convers to .bam file

"""

import sys, re, pysam
from math import floor

start = ''
store = []
last_pos = None
new_pos = None
count = 0

samfile = pysam.AlignmentFile(sys.argv[1], 'rb')

for i in samfile.fetch():
    #print i
    if i.has_tag('AN'):
        if i.is_reverse:
            #start = str(i.pos)
            start = i.pos
            end = start
            ref_id = i.reference_id
            name = samfile.getrname(ref_id)
            
            v = floor(start/50) * 50
            #store = [name, start, v, count]
            if count > 0:
                if v in store:
                    count += 1
                    store.pop()
                    store.append(count)
                else:
                    #print store
                    #print ' '.join([store[0], str(int(store[2])), str(int(store[2]))])
                    print ' '.join([store[0], str(int(store[2])), str(int(store[3]))])
                    count = 0
            else:
                count += 1
                store = [name, start, v, count]
#print store
            #if new_pos == last_pos:
            #    count += 1
            #else:
            #    print name, start, v, count
            #last_pos == new_pos
#            print '\t'.join([name,
#                             source,
#                             polya,
#                             start,
#                             end,
#                             place_holder,
#                             strand,
#                             place_holder,
#                             attributes])
#        else:
#            start = str(i.reference_end)# i.pos+i.reference_length
#            end = start
#            strand = '+'
#            ref_id = i.reference_id
#            name = samfile.getrname(ref_id)
#            m = re.search('chr*[^_]+', name)
#            attributes = ';'.join([color, 'id='+i.qname])
#
#            print '\t'.join([name,
#                             source,
#                             polya,
#                             start,
#                             end,
#                             place_holder,
#                             strand,
#                             place_holder,
#                             attributes])
# 
