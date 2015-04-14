#!/usr/bin/python

import sys

last_pos = None
new_pos = None
chrom_name = None

for i in sys.stdin:
    
    new_pos = i.split()[2]
    chrom_name = i.split()[0]

    if new_pos == last_pos:
        continue
    
    else:
        print i.strip()

    last_pos = new_pos
