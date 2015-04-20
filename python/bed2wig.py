#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

"""

This reads in from standard out from bin_wig.py file and further modifies to wig format, by appending Track line and
Chromosome lines. 

"""

import sys

#input your chromosome name format, reaplace chromosome number with an n
#provide number of chromosomes
#provide any other additional chromosome names. e.g mitochondrial chromosome 
#type out a full name of the chromosome exactly as it appears in the file
#including all the file cases.

track = 'track'
file_type = 'type=wiggle_0'
#name = 'Verma-Gaur et al., PAS forward'
name = "Verma-Gaur et al., PAS reverse"
step = 'variableStep'
span = 'span=1'
chname = None
ch = 'chrom=%s'

first_line = [track, file_type, name]
chline = [step, "chrom=%s", span]

for i in sys.stdin:
    line = i.strip().split()
    value = line[1]
    depth = line[2]

    if chname:
        if chname == line[0]:
            print value, depth
        else:
            chname = line[0]
            print ' '.join([step, ch  % chname, span])
            print value, depth
    else:
        print ' '.join(first_line)
        chname = line[0]
        print ' '.join([step, ch  % chname, span])
        print value, depth
