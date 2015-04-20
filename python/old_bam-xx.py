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

def compare2(arg1, arg2):
    old_itme = return_count(arg1)
    new_item = return_cout(arg1)
    if old_item == new_item:
        return arg2
    else:
        count_log(arg2)

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
count = 0
ch_dict = {}

#check = [int(i.split(':')[0]) for i in store]

for i in sys.stdin:
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
            #print name, pos
            while name == 'Ca19-mtDNA':
                item = int2str(pos)
                #check = [int(i.split(':')[0]) for i in store]
                if item not in store:
                    store.append(item)
                else:
                    new_item = count_log(item)
                    store.append(new_item)
                #else:
                #    print 'Inside else'

for i in store:
    print i
#                key = make_key(name, pos)
#                if key not in ch_dict.keys():
#                    ch_dict[key]=1
#                else:
#                    temp = ch_dict.get(key)
#                    count = temp + 1
#                    ch_dict[key]=count
#                    temp = None
#
#for key, value in ch_dict.items():
#    print key, value
#               

            
