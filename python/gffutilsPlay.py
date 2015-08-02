#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
import gffutils, sys

#check = gffutils.example_filename('intro_docs_example.gff')
myGFF = sys.argv[1]
#myGFF = open(sys.argv[1]).readline()

#db = gffutils.create_db(myGFF, dbfn='PasteurellaMultocida-Pm70.db', force=True, keep_order=True, merge_strategy='merge', sort_attribute_values=True)
db = gffutils.create_db(myGFF, dbfn='Mus_musculus_GFF.db', force=True, keep_order=True, merge_strategy='merge', sort_attribute_values=True)
#db = gffutils.FeatureDB('test.db', keep_order=True)
#db = gffutils.FeatureDB('PasteurellaMultocida-Pm70.db', keep_order=True)

#print dir(db)
#print gffutils.constants.SCHEMA
#print dir(gffutils)
#print help(gffutils.Feature)
#print dir(gffutils.FeatureDB)
#print help(gffutils.parser)
#print dir(gffutils.feature)
#print help(gffutils.feature)
#print help(gffutils.feature.feature_from_line)
#print type(gffutils.feature.feature_from_line(myGFF))
#check = gffutils.feature.feature_from_line(myGFF)
#print dir(check)
#print check
# Thats simply all features. Check
#check = db.all_features()
#check = db.bed12
#print help(check)
#for i in check:
#   #print dir(i)
#   print db.bed12(i)
#   print '------------'
#print help(db.bed12)
#gene = db['gene2']
#
#for i in db:
#    print i
