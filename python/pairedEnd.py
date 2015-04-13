#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

import sys, os

#path = 'data/cell-free-rna'
#path = 'working_dir'
path = sys.argv[1]

total_fq_count = len([name for name in os.listdir(path) if name.endswith('fastq.gz')])
total_r2_count = len([read for read in os.listdir(path) if 'R2' in read.upper()])

if total_fq_count > 0:
    if total_r2_count > 0:
        if float(total_r2_count) == float(total_fq_count)/2:
            print True
        else:
            print "Number of R1 reads doesn't match up with R2 reads in the `%s` directory" % path
    else:
        print 'No paired read found in the `%s` directory' % path
else:
    print 'No fastq files found in the `%s` directory' % path
