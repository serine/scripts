#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

"""
16 == negative strand
0 == positive strand
"""

def make_key(name, pos):
    n = str(name)
    p = str(pos)
    np = ':'.join((n,p))
    return np

def return_count(c):
    return int(c.split(':')[1])

def freturn(pos, item):
    p = int(pos)
    i = item.split(':')
    if p == int(i[0]):
        oneup = int(i[1])+1
        return fmake(p, oneup)

def fmake(number, count):
    n = str(number)
    c = str(count)
    return  n+':'+c
       

def count_log(c):
    split = c.split(':')
    pos = int(split[0])
    count = int(split[1])
    new_count = count + 1
    return str(pos)+':'+str(new_count)
    
def int2str(pos):
    p = str(pos)
    return  p+':'+'1'

def str2int(arg1):
    a = arg1.split(':')[0]
    return int(a)

import sys
from collections import defaultdict

store = []
check = ''

#f = open(sys.argv[1])

for i in sys.stdin:
#for i in f: 
    line = i.strip()
    if 'AA' in line:
        read = line.split()
        name = read[1]
        strand = int(read[0])
        pos = int(read[2].split(':')[2])
        if strand == 16:
            pass
        #    #print name, strand, pos
        #    if count > 0:
        #        if pos in store:
        #            count += 1 
        #            store.pop()
        #            store.append(count)
        #        else:
        #            if count > 5:
        #                print ' '.join([store[0],
        #                               str(store[1]),
        #                               str(store[2]),
        #                               str(store[3])
        #                               ])
        #            count = 0
        #    else:
        #        count += 1
        #        store = [name, strand, pos, count]

        else:
            item = fmake(pos, 1)
            
            if pos not in [int(i.split(':')[0]) for i in store]:
                store.append(item)

            else:
                #print pos,\
                #      item,\
                #      store.index(item),\
                #      [int(i.split(':')[0]) for i in store].index(pos),\
                #      'Not in store'
                temp_index = [int(i.split(':')[0]) for i in store].index(pos)
                temp_item = store.pop(temp_index)
                new_item = count_log(temp_item)
                store.insert(temp_index, new_item)

for i in store:
    print i
