#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

import gffutils, sys

myGFF = sys.argv[1]
dbName = sys.argv[2]

#------------------------
# Creates a database file
#------------------------
db = gffutils.create_db(
    myGFF,
    args.database,

    # Since Ensembl GTF files now come with genes and transcripts already in
    # the file, we don't want to spend the time to infer them (which we would
    # need to do in an on-spec GTF file)
    disable_infer_genes=True,
    disable_infer_transcripts=True,

    # Here's where we provide our custom id spec
    id_spec=id_spec,

    # "create_unique" runs a lot faster than "merge"
    # See https://pythonhosted.org/gffutils/database-ids.html#merge-strategy
    # for details.
    merge_strategy='create_unique',
    verbose=True,
    force=args.force,
)
#----------------------------------------------------------------------------------------------------
