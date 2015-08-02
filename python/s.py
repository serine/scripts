#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
from Bio import SeqIO
import sys

f = open(sys.argv[1])
for i in SeqIO.parse(f, 'fasta'):
#for i in f:
    #if i.startswith(">"):
    #   print i
    print i.id, len(i.seq)
