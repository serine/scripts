#!/usr/bin/env python

import sys
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

threshold = 0
#chrom =">Chr%s"
bootstrap = 'length %s, coverage %s'
for record in SeqIO.parse(open(sys.argv[1]), 'fasta'):
    splitID = record.id.split("_")
    coverage = float(splitID[-3])
    if coverage > threshold:
        name = ''.join((splitID[0], splitID[1]))
        length = splitID[3]
        coverage = splitID[5]
        info = bootstrap % (length, coverage)
        seqRecord = SeqRecord(seq=record.seq, id=name, description=info)
        #print coverage, record.id
    #print '\t'.join([seqRecord.id, str(len(seqRecord.seq))])
    #print seqRecord.id, len(seqRecord.seq)
    #if seqRecord.id.startswith('NODE_2_length_84994'):
        SeqIO.write(seqRecord, sys.stdout, 'fasta')
