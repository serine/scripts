#!/usr/bin/python

from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import sys


f = open(sys.argv[1])

threshold = 0
bootstrap = 'length %s coverage %s'

for record in SeqIO.parse(f, 'fasta'):
    splitID = record.id.split("_")
    coverage = float(splitID[-3])
    if coverage > threshold:
        name = ''.join((splitID[0], splitID[1]))
        length = splitID[3]
        coverage = splitID[5]
        info = bootstrap % (length, coverage)
        seqRecord = SeqRecord(seq=record.seq, id=name, description=info)
        #print coverage, record.id
        SeqIO.write(seqRecord, sys.stdout, 'fasta')
