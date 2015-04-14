#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

import sys
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

#f = open(sys.argv[1])
chrom_name = 'chr%s'
test = ''

for seq_record in SeqIO.parse(sys.argv[1], 'fasta'):

    ##########    Section One  ################
    #chrom_name_temp = seq_record.id.split('Chr')
    #test = chrom_name % chrom_name_temp[1]
    #new_record = SeqRecord(seq_record.seq, id=test, name='', description='')
    #SeqIO.write(new_record, sys.stdout, 'fasta')


    ##########   Section Two  ################

    print '\t'.join([str(seq_record.id), str(len(seq_record.seq))])
