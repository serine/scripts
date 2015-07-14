#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
#!/usr/bin/env python

from Bio import SeqIO
from Bio import SeqRecord

import sys, argparse

def open_either(file, mode='r'):
    '''open either compressed or not compressed files'''
    if file.endswith('.gz'):
        import gzip
        return gzip.open(file, mode)
    else:
        return open(file, mode)
        
        
def calc_percentA(List):
    BaseList = ['A']
    for Base in BaseList:
        Percent = 100 * List.count(Base) / float(len(List))
        PercentA = float(Percent)
    return PercentA  

def calc_percentC(List):
    BaseList = ['C']
    for Base in BaseList:
        Percent = 100 * List.count(Base) / float(len(List))
        PercentC = float(Percent)
    return PercentC        
    
def calc_percentG(List):
    BaseList = ['G']    
    for Base in BaseList:
        Percent = 100 * List.count(Base) / float(len(List))
        PercentG = float(Percent)
    return PercentG
    
def calc_percentT(List):
    BaseList = ['T']    
    for Base in BaseList:
        Percent = 100 * List.count(Base) / float(len(List))
        PercentT = float(Percent)
    return PercentT
    
        
if __name__ == '__main__' :

    parser = argparse.ArgumentParser(description='Filter paired-end read quality based on percent base composition.',)    
    
    parser.add_argument('-1', '--fastq1', help='The input read1 fastq file.', required=True)
    parser.add_argument('-2', '--fastq2', help='The input read2 fastq file.', required=True)
    parser.add_argument('-p', '--minPercent', help='Any base must account for this percent of read. Or read will be discarded.', type=float, default=5.0)
    parser.add_argument('-o1', '--outFile1', help='fastq1 output file.', required=True)
    parser.add_argument('-o2', '--outFile2', help='fastq2 output file.', required=True)    

    args = parser.parse_args()

    fastqFormat = 'fastq'
    

    fastq1handle = open_either(args.fastq1, 'rU')
    fastq2handle = open_either(args.fastq2, 'rU')

    fastq1out = open_either(args.outFile1, 'wb')
    fastq2out = open_either(args.outFile2, 'wb')
    
    fastq1SeqIO = SeqIO.parse(fastq1handle, fastqFormat)
    fastq2SeqIO = SeqIO.parse(fastq2handle, fastqFormat)
    
    
    while True:
        
        try:
            
            fastq1record = fastq1SeqIO.next()
            fastq2record = fastq2SeqIO.next()
            
        except:
        
            break
            
        Seq_ListR1 = fastq1record.seq
        Seq_ListR2 = fastq2record.seq        
    
    
        if (calc_percentA(Seq_ListR1) < args.minPercent) or (calc_percentA(Seq_ListR2) < args.minPercent):
            continue
            
        if (calc_percentC(Seq_ListR1) < args.minPercent) or (calc_percentC(Seq_ListR2) < args.minPercent):
            continue
            
        if (calc_percentG(Seq_ListR1) < args.minPercent) or (calc_percentG(Seq_ListR2) < args.minPercent):
            continue            
        
        if (calc_percentT(Seq_ListR1) < args.minPercent) or (calc_percentT(Seq_ListR2) < args.minPercent):
            continue
                
        
        fastq1out.write(fastq1record.format(fastqFormat))
        fastq2out.write(fastq2record.format(fastqFormat))
    
    fastq1out.close()
    fastq2out.close()
        
        
    print "Filtering complete!"
