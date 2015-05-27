#!/usr/bin/env python

import sys
from Bio import SeqIO

#chrom =">Chr%s"

for seqRecord in SeqIO.parse(open(sys.argv[1]), 'fasta'):
    print '\t'.join([seqRecord.id, str(len(seqRecord.seq))])
    #print seqRecord.id, len(seqRecord.seq)
