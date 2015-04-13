#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

class DNASequence:

    def __init__(self, sequence):
        self.sequence = sequence
        self.base_counts = {}

    def base_count(self, base):
        if base in self.base_counts:
            return self.base_counts[base]
        else:
            count = self.sequence.count(base)
            self.base_counts[base] = count
            return count

    def gc_content(self):
        g = self.base_count('G')
        c = self.base_count('C')
        return float(g+c)/len(self.sequence)

    def reverse_complement(self):
        complements = {'G': 'C',
        'C': 'G',
        'A': 'T',
        'T': 'A'}
        rev_c = ""
        for base in self.sequence:
            rev_c = complements[base] + rev_c
            return rev_c

    def upper_case(self):
        string = str(self.sequence)
        return string.upper()
        #return self.sequence


