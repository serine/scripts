#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import sys

f = open(sys.argv[1])

for i in SeqIO.parse(f, 'genbank'):
    record = SeqRecord(i.seq, id=i.id, description='')
    SeqIO.write(record, sys.stdout, 'fasta')
