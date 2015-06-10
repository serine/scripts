#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
import os
import sys
 
#working_dir = '/data/HD/analysis/038ea/analysis/1/fastqc/'
working_dir = sys.argv[1]
 
fastqc_summary = open(working_dir+'fastqc_summary.txt',mode='wb')
fastqc_details = open(working_dir+'fastqc_details.txt',mode='wb')
 
for root, dirs, files in os.walk(working_dir): # walk a directory containing FastQC output for multiple samples
    for name in files:
        if (name == "fastqc_data.txt"):
            fileid = fileid = root.split("/")[-1][:-7] # use string slicing here if you only want part of the filename as the id
            with open(os.path.join(root,name),"r") as f: # automatically close the file when done
                for line in f.readlines():
                    line = line.strip() # trim endline
                    if (line[:2] == ">>" and line[:12] != ">>END_MODULE"): # for each module grab summary data
                        module = line[2:-5] # grab module name
                        status = line[-4:] # and overall status pass/warn/fail
                        fastqc_summary.write(fileid+"\t"+module+"\t"+status+"\n")
                        #sql = "insert into fastqc_summary(fileid,module,status) values(%s,%s,%s);"
                        #data = (fileid,module,status)
                        #c.execute(sql,data)
                    elif (line[:2] != ">>" and line[:2] != "##"): # grab details under each module
                        cols = line.split("\t")
                        col1 = cols[0]
                        ocols = "|".join(cols[1:])
                        fastqc_details.write(fileid+"\t"+module+"\t"+col1+"\t"+ocols+"\n")
                        #sql = "insert into fastqc_details(fileid,module,col1,ocols) values(%s,%s,%s,%s);"
                        #data = (fileid,module,col1,ocols)
                        #c.execute(sql,data)
 
fastqc_summary.close()
fastqc_details.close()
