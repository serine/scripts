#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
import gffutils, sys
import string, random

#myGFF = sys.argv[1]

#--------------------------------------------------
# Firstly you need to create a database file
# You can use command below or make-gtf-db.py scrip
#--------------------------------------------------
#db = gffutils.create_db(myGFF, dbfn='PasteurellaMultocida-Prokka.db', force=True, keep_order=True, merge_strategy='merge', sort_attribute_values=True)
#db = gffutils.create_db(myGFF, dbfn='x73WT.db', force=True, keep_order=True, merge_strategy='merge', sort_attribute_values=True)
#db = gffutils.create_db(myGFF, dbfn='Mus_musculus_GFF.db', force=True, keep_order=True, merge_strategy='merge', sort_attribute_values=True)
#----------------------------------------------------------------------------------------------------

#------------------------------
# Main body
#------------------------------

#db = gffutils.FeatureDB('Mus_musculus.GRCm38.80.db', keep_order=True)
#db = gffutils.FeatureDB('PasteurellaMultocida-Pm70.db', keep_order=True)
#db = gffutils.FeatureDB('PasteurellaMultocida-Prokka.db', keep_order=True)
db = gffutils.FeatureDB('x73WT.db', keep_order=True)

#------------------------------
# Learn the database attributes
#------------------------------
#dbDirList = dir(db)
#for i in dbDirList:
#   if not i.startswith('__'):
#       print i

# _autoincrements
# _execute
# _feature_returner
# _insert
# _method_doc
# _relation
# _update
# add_relation
# all_features
# bed12
# children
# children_bp
# conn
# count_features_of_type
# create_introns
# dbfn
# default_encoding
# delete
# dialect
# directives
# execute
# features_of_type
# `featuretypes` returns a all unique features type in the gtf file
# interfeatures
# iter_by_parent_childs
# keep_order
# merge
# method
# parents
# pragmas
# region
# schema
# set_pragmas
# sort_attribute_values
# update
# version

#----------------------------------------------------------------------------------------------------

#print help(db.features_of_type)
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

#-----------------------------------
# All methods on each fature line 
#-----------------------------------
featureLine = db.all_features()
# astuple
# attributes
# bin
# calc_bin
# chrom
# dialect
# end
# extra
# featuretype
# file_order
# frame
# id
# keep_order
# score
# seqid
# sequence
# sort_attribute_values
# source
# start
# stop
# strand
#----------------------------------------------------------------------------------------------------

check = False
l = []
for i in featureLine:
    #if i.featuretype == 'exon' or i.featuretype == 'CDS':
    #   print db.bed12(i)

    #if i.featuretype == 'gene':
    if i.featuretype == 'CDS':
        locusId = i.attributes.get('locus_tag').pop()
        l.append(locusId)
        #print i.attributes['locus_tag']
        #print locusId

    #if not i.featuretype == 'gene' and not i.featuretype == 'region':
    #if i.featuretype == 'CDS' or i.featuretype == 'exon':
    if i.featuretype == 'exon' or i.featuretype == 'CDS':
        check = True
    #------------------------------
    # All possible attributes names
    #------------------------------
    # anticodon
    # Dbxref
    # end_range
    # exception
    # gbkey
    # gene
    # genome
    # ID
    # Is_circular
    # mol_type
    # Name
    # ncrna_class
    # Note
    # Parent
    # partial
    # product
    # protein_id
    # pseudo
    # strain
    # sub-species
    # transl_except
    # transl_table
    #------------------------------
    #if not i.featuretype == 'gene':
        tag = i.attributes

        #if tag.get('Dbxref'):
        #   uniqId = tag.get('Dbxref').pop()
        #   l.append(uniqId)
        #   #print uniqId
        #else:
        #   l.append('.')
        #   #print '-'

        #if tag.get('gene'):
        #   geneName = tag.get('gene').pop()
        #   l.append(geneName)
        #else:
        #   #gotIt = 'RanStr-'+ ''.join(random.choice(string.lowercase) for x in range(5))
        #   gotIt = '-'
        #   l.append(gotIt)

        #if tag.get('Name'):
        #   wpId = tag.get('Name').pop()
        #   l.append(wpId)
        #else:
        #   l.append('-')

        if tag.get('product'):
            geneProduct = tag.get('product').pop()
            l.append(geneProduct)
        else:
            l.append('-')
        
        #if tag.get('ID'):
        #   geneProduct = tag.get('ID').pop()
        #   l.append(geneProduct)
        #else:
        #   l.append('-')

    if check:
        t = '\t'.join(l)
        #print '\t'.join((db.bed12(i, block_featuretype=['CDS'], name_field='Dbxref'), t))
        print '\t'.join((db.bed12(i, name_field='ID'), t))
        #print db.bed12(i, name_field='ID')
        #print db.bed12(i)
        l = []
        check = False
    #--------------------------------------------------
    #geneId = i.attributes['gene_id'][0]
    #geneName = i.attributes['gene_name'][0]
    ##print help(db.bed12)
    ##break
    #if not i.featuretype == 'gene':
    #   if i.featuretype == 'transcript':
    #       transcriptId = i.attributes['transcript_id'][0]
    #       #bed12line = db.bed12(i, thick_featuretype=['exon'], name_field='transcript_id')
    #       bed12line = db.bed12(i, name_field='transcript_id')
    #       print '\t'.join((bed12line, geneId, geneName))
    #       #print bed12line
