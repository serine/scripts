#! /usr/bin/env python

"""
parsers a .bam file and grabs poly(A) end positions and writes to .gff file

"""

import sys, re, pysam

samfile = pysam.AlignmentFile(sys.argv[1], 'rb')
counter = 0

#with open(sys.stdout, w) as fout:
source = 'python'
polya = 'poly(A)tail'
start = ''
strand = ''
place_holder = '.'
color = 'color=#0000ff'
attributes = ''

for i in samfile.fetch():
    #print help(i)
    #break
    if i.has_tag('AN'):
        if i.is_reverse:
            start = str(i.pos)
            end = start
            strand = '-'
            ref_id = i.reference_id
            name = samfile.getrname(ref_id)
            attributes = ';'.join([color, 'id='+i.qname])

            print '\t'.join([name,
                             source,
                             polya,
                             start,
                             end,
                             place_holder,
                             strand,
                             place_holder,
                             attributes])
        else:
            start = str(i.reference_end)# i.pos+i.reference_length
            end = start
            strand = '+'
            ref_id = i.reference_id
            name = samfile.getrname(ref_id)
            m = re.search('chr*[^_]+', name)
            attributes = ';'.join([color, 'id='+i.qname])

            print '\t'.join([name,
                             source,
                             polya,
                             start,
                             end,
                             place_holder,
                             strand,
                             place_holder,
                             attributes])

