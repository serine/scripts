#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

import sys

for i in open(sys.argv[1]):
    line = i.split("\t")
    line.pop(3)
    line.insert(3, "")
    print "\t".join(line)
