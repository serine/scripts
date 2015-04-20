#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

import sys

f = open(sys.argv[1])

for i in f:
    if i.startswith('>Ca'):
        print i
