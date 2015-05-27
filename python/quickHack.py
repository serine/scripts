#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
import sys
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import IUPAC

for i in open(sys.argv[1]):
    line = i.strip().split(',')
    #print line[0], line[1].strip()
    record = SeqRecord(seq=Seq(line[1].strip()), id=line[0], name='', description='')
    SeqIO.write(record, sys.stdout, 'fasta')
    #print record
