#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

import sys

for i in sys.argv[1]:
    if 'R1' in i:
        print i
    else:
        print 'paired read'
