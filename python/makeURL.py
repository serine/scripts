#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
import sys, os, re

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split('(\d+)', text) ]
'''
include number of reads
sort them
'''

dataDir = sys.argv[1]
listOfFiles = os.listdir(dataDir)

chromosome = 2
start = 132900815
end = 132915021

header = True

localHost = 'http://localhost:60151/load?file=http%3A%2F%2Fbioinformatics.erc.monash.edu'
theServer = 'http%3A%2F%2Fbioinformatics.erc.monash.edu'

trackInfoTemplate = '%s&genome=mm10&merge=true&name=%s&locus=chr%s:%s-%s'

print "<h4><a href='igv.jnlp'>Click this link to launch IGV</a></h4>"
print "<table class='check' border=1 frame=void rules=all align=center cellpadding=5px>"
for i in sorted(listOfFiles, key=natural_keys):
    if i.endswith('bam'):
        getFullPath = os.path.abspath(dataDir)
        getRightPathIndex = getFullPath.index('/home/kirill')
        getRightPath = getFullPath[getRightPathIndex:]+'/'
        urlPath = localHost+getRightPath.replace('/', '%2F')
        bamFile = os.path.join(getRightPath, i)

        name = i.strip().split("_")[0]
        bamName = name+'.sorted.bam'
        trackInfo = trackInfoTemplate % (i, name, chromosome, start, end)
        if header:
            print '<tr><td>IGV links</td><td>BAM files</td><tr>'
            header = False

        print '<tr><td><a href="%s">%s</a></td><td><a href="%s">%s</a></td></tr>' % (urlPath+trackInfo, name, bamFile, bamName)
print "</table>"
