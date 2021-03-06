#! /usr/bin/env python

"""
This script only output Forward OR Reverse. Need to change the flag
on line 29

parsers a .bam file and grabs poly(A) end positions, checks how many of those
have been repeated and gives the depths of the repeats
outfile is space delimited

This is an intermediate step to a wiggle file

"""

import sys, re, pysam

samfile = pysam.AlignmentFile(sys.argv[1], 'rb')

threshold = 0
check = ''
store = {}
last_name = ''

for i in samfile.fetch():

    if i.has_tag('AA'):
        # `not` is used here to switch between forward of reverse strands
        # `if not` means Forward strand
        # `if` is a reverse strand
        if not i.is_reverse:
            start = i.get_tag('AA') 
            ref_id = i.reference_id
            name = samfile.getrname(ref_id)
    print samfile.getrname(i.rname)
#           if name == check:
#               last_name = name
#               
#               if start not in store:
#                   store[start]=1
#               store[start]+=1
#           else:
#               check = name
#
#               if store:
#                   for i in iter(sorted(store.iteritems())):
#                       if i[1] > threshold:
#                           print last_name, i[0], i[1]
#
#               store = {}
#               store[start]=1
#
## this output very last chromosome
#if store:
#   for i in iter(sorted(store.iteritems())):
#       if [i] > threshold:
#           print last_name, i[0], i[1]
