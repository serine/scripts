#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split('(\d+)', text) ]

import sys, re, os, argparse

parser = argparse.ArgumentParser(description="blah blah")

parser.add_argument('--vcfFiles', nargs=1, help="specify directory with vcf files")
parser.add_argument('--bamFiles', nargs=1, help="specify directory with bam files")

if len(sys.argv)==1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()
vcfFiles = args.vcfFiles[0]
bamFiles = args.bamFiles[0]

vcfs = os.listdir(vcfFiles)
bams = os.listdir(bamFiles)

header = True
#threshold = 0
threshold = 1000
firstSample = True

rootURL = 'http://localhost:60151/load?file=http%3A'
host = '2F%2Fbioinformatics.erc.monash.edu'
path = '2Fhome%2Fkirill%2FMichelleMeilak%2FbamFiles'
igvTemplate = '2F%s&genome=mm10&merge=true&name=%s&locus=%s'

print "<table class='vcf' border=1 frame=void rules=all align=center cellpadding=5px>"

for item in sorted(vcfs, key=natural_keys):
    if item.endswith(".vcf"):
        vcfFile = open(os.path.join(vcfFiles, item))
        #--------------------------------------------------
        # py magic
        #--------------------------------------------------
        #bamFile = open(os.path.join(bamFiles, item.split("_")[0]+"_sorted.bam"))
        bamFile = item.split("_")[0]+"_sorted.bam"
        tmpName =item.split("_")[0]
        name = 'Sample-%s' % tmpName
        counter=0
        check=''

        if header:
            print "<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % ("Chrom", "Position", "Reference", "Alternative", "Depth")
            #print "<td>%s</td>" % name
            header = False
            
        for i in vcfFile:
            items = i.strip().split()

            if not i.startswith("#"):
                m = re.search("(DP=)([0-9]+)", items[7])
                depth = int(m.group(2))
                chrom = items[0]
                position = int(items[1])
                upstream = position-200
                downstream = position+200
                locus = "%s:%s-%s" % (chrom, upstream, downstream)
                igvLink = igvTemplate % (bamFile, bamFile, locus)
                if m and depth > threshold:
                    #print "<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % (items[0], items[1], items[3], items[4], m.group(0))
                    igv =  '<a href="%s">%s</a>' % ('%'.join([rootURL, host, path, igvLink]), position)
                    #check+="<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>\n" % (items[0], items[1], items[3], items[4], m.group(0))
                    #check+="<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>\n" % (chrom, igv, items[3], items[4], m.group(0))
                    check+="<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>\n" % (chrom, igv, items[3], items[4], depth)
                    counter+=1

        if counter > 0:
            #print "<tr bgcolor=#FFFFE0><td></td><td><b>%s</b></td><td></td><td></td><td></td></tr>" % name
            print "<tr><td></td><td><b>%s</b></td><td></td><td></td><td></td></tr>" % name
            print check.strip()
        elif counter == 0:
            #print "<tr bgcolor=#FFE0E0><td></td><td><b>%s</b></td><td>%s</td><td></td><td></td></tr>" % (name, 'no significant SNPs or InDels was identified')
            print "<tr><td></td><td><b>%s</b></td><td>%s</td><td></td><td></td></tr>" % (name, 'no significant SNPs or InDels was identified')

        #if counter == 0:
        #   print "<tr><td>%s</td><td></td><td>%s</td><td></td><td></td></tr>" % ("hey", name)
print "</table>"
