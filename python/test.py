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
listOfFiles = os.listdir(sys.argv[1])

rootURL = 'http://localhost:60151/load?file=http'
host = '3A%2F%2Fbioinformatics.erc.monash.edu'
filesDits = '2Fhome%%2Fkirill%%2FMichelleMeilak%%2FbamFiles%%2F%s&genome=mm10&merge=true&name=%s&locus=chrX:56,789,838-56,790,061'
sample = 'sample-%s'

#rootURL = 'http://localhost:60151/load?file=http'
#host = '3A%2F%2Fbioinformatics.erc.monash.edu'
#dirRoot = '2Fhome%%2Fkirill%%2FMichelleMeilak%%2FbamFiles%%2F%s&genome=mm10&merge=true&name=%s&locus=chrX:56,789,838-56,790,061'
#filesDits = "check%%blah%%foo %s"
print "<h4><a href='igv.jnlp'>Launch IGV</a></h4> \n <ul>"
for i in sorted(listOfFiles, key=natural_keys):
    if i.endswith('bam'):
        #print FilesDits % (i)
        preName = i.strip().split("_")[0]
        name = sample % preName
        igvLink = filesDits % (i, name)
        print '<li>%s <a href="%s">IGV link</a></li>' % (name, '%'.join([rootURL, host, igvLink]))
print "</ul>"
