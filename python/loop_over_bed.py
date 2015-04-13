#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

import sys

f = open(sys.argv[1])

chrom_name = 'chr%s'
temp_chrom_name = 'Ca21chr%s_C_albicans_SC5314'

for i in f:
    if i.startswith('Ca19-mtDNA'):
        pass
    else:
        chrom_number = i.split()[0].split('_')[0].split('chr')[1]
        #print chrom_name % chrom_number
        #print i.replace('Ca21chr1_C_albicans_SC5314', 'test')
        old_chrom_name = temp_chrom_name % chrom_number
        new_chrom_name = chrom_name % chrom_number
        print i.replace(old_chrom_name, new_chrom_name)

