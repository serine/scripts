#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

import sys

f = open(sys.argv[1])

for miss in range(1):
    f.next()

for i in f:
    print i.strip().split()
