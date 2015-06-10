#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

import sys
from Bio import SeqIO

for i in SeqIO.parse(sys.argv[1], 'fasta'):
    print i.id, len(i.seq)
