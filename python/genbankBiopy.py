#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import sys

for i in SeqIO.parse(open(sys.argv[1]), 'genbank'):
    SeqIO.write(i, sys.stdout, 'fasta')
