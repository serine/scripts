#!/usr/bin/python

import sys
   
f = open(sys.argv[1])

pos = []
neg = []

for i in f:
    #print i.strip().split()
    if i.split()[6] == '+':
        pass
        #pos.append(i.split()[3])
    else:
        neg.append(i.split()[3])
#print int(len(set(pos)))+int(len(set(neg)))
print len(neg), len(set(neg))
    
    #last_pos = i.split()[3]
    #print i.strip(), last_pos, new_pos
    #if new_pos != last_pos:
    #    print i.strip(),'--------', last_pos, new_pos

#    current_pos = i.split()[3]
#    next_line = f.next()
#    next_pos = next_line.split()[3]
#    if current_pos != next_pos:
#        print current_pos
#        print next_pos
#    else:
#        current_pos = next_pos
#        print current_pos
