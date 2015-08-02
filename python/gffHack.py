#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

import sys, re, os

f = open(sys.argv[1])

geneName = None
transcriptName = None
previousTranscriptName = None

exonName = None
previousExonName = None

exonListBefore = []
exonListAfter = []
exonLengths = []
exonBaseLengths = []

score = str(1000)
thinkStart = str(0)
thinkEnd = str(0)
rgb = "0,0,0"

baseExon = None

for i in f:

    #c = re.search('((chr([0-9]+|[A-Z])|([A-Za-z0-9]+.[0-9]))\t)', i.strip())
    #c = re.search('(([0-9]|[A-Z]+)|(([A-Za-z0-9]+)|(([^A-Za-z0-9][A-Za-z0-9]+)|\w+.\d)))\t', i.strip())
    c = re.search('([A-Za-z0-9_]+(\.[0-9])?)\t', i.strip())
    g = re.search('(gene_id\s")([A-Za-z0-9]+.[0-9])', i.strip())
    n = re.search('(gene_name\s")([A-Za-z0-9]+)', i.strip())
    e = re.search('(transcript_id\s")([A-Za-z0-9]+.[0-9])', i.strip())
    t = re.search('(transcript_id\s")([A-Za-z0-9]+.[0-9])', i.strip())
    #b = re.search('(gene_type\s")([A-za-z0-9]+)', i.strip())
    b = re.search('(gene_biotype\s")([A-za-z0-9_]+)', i.strip())
    m = re.search('(exon\t)([0-9]+)\t([0-9]+)', i.strip())
    s = re.search('\t(\.)\t([^0-9])\t(\.)\t', i.strip())

    tc = re.search('(\t)(transcript)(\t)', i.strip())

    if tc:
        #print tc.groups()
        transcriptString = tc.string
        tm = re.search('(transcript\t)([0-9]+)\t([0-9]+)', i.strip())
        transcriptCo = '\t'.join((tm.group(2), tm.group(3)))
    if m:
        #print g.groups(), m.groups(), t.groups()
        chromosome = c.group(1)
        geneName = g.group(2)
        publicName = n.group(2)
        exonStart = int(m.group(2))
        exonEnd = int(m.group(3))
        transcriptName = t.group(2)
        exonName = e.group(2)
        exonLength = str(exonEnd-exonStart)
        strand = s.group(2)
        biotype = b.group(2)
        

        if transcriptName != previousTranscriptName:
            baseExon = None
            if exonListBefore:
                print '\t'.join(('\t'.join(exonListBefore), thinkStart, thinkEnd, rgb, str(len(exonLengths)), ','.join(exonLengths), ','.join(exonBaseLengths), '\t'.join(exonListAfter)))
                exonListBefore = []
                exonListAfter = []
                exonLengths = []
                exonBaseLengths = []
                baseExon = None

        if not baseExon:
            baseExon = exonStart
        baseExonStart = str(abs(exonStart-baseExon))

        if (chromosome and transcriptCo and transcriptName and strand) not in exonListBefore:
            exonListBefore.append(chromosome)
            exonListBefore.append(transcriptCo)
            exonListBefore.append(transcriptName)
            exonListBefore.append(score)
            exonListBefore.append(strand)

        if (geneName and publicName and biotype) not in exonListAfter:
            exonListAfter.append(geneName)
            exonListAfter.append(publicName)
            exonListAfter.append(biotype)

        if strand == "+":
            exonLengths.append(exonLength)
        #   baseExonStart = str(exonStart-baseExon)
        else:
            exonLengths.insert(0,exonLength)
        #   baseExonStart = str(baseExon-exonStart)
        #exonLengths.append(exonLength)
        exonBaseLengths.append(baseExonStart)

        previousExonName = exonName
        previousTranscriptName = transcriptName
