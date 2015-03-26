#! /usr/bin/env python

"""
parsers a .bam file and grabs poly(A) end positions and writes to .gff file

Notes of PySam


"""

import sys, re, pysam

samfile = pysam.AlignmentFile(sys.argv[1], 'rb')
counter = 0

source = 'python'
polya = 'poly(A)tail'
start = ''
strand = ''
place_holder = '.'
color = 'color=#0000ff'
attributes = ''

for i in samfile.fetch():
    #print i.get_tag('AA')
    #print help(i)
     #print i.get_tag('AA')
    #break
#     if i.has_tag('AN'):
#         if i.is_reverse:
#             start = str(i.pos)
#             end = start
#             strand = '-'
              #to get a reference name you need to get ID and call samfile.getrname() on it
#             ref_id = i.reference_id
#             name = samfile.getrname(ref_id)
#             attributes = ';'.join([color, 'id='+i.qname])
# 
#             print '\t'.join([name,
#                              source,
#                              polya,
#                              start,
#                              end,
#                              place_holder,
#                              strand,
#                              place_holder,
#                              attributes])
#         else:
#             start = str(i.reference_end)# i.pos+i.reference_length
#             end = start
#             strand = '+'
#             ref_id = i.reference_id
#             name = samfile.getrname(ref_id)
#             #m = re.search('chr*[^_]+', name)
#             attributes = ';'.join([color, 'id='+i.qname])
# 
#             print '\t'.join([name,
#                              source,
#                              polya,
#                              start,
#                              end,
#                              place_holder,
#                              strand,
#                              place_holder,
#                              attributes])
