import argparse, sys

#creat optional arguments using argparse module
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--infile', nargs=1, type=argparse.FileType('r'))
parser.add_argument('-o1', '--outfile_one', nargs='?', type=argparse.FileType('w'))
parser.add_argument('-o2', '--outfile_two', nargs='?', type=argparse.FileType('w'))
args = parser.parse_args()
#take the first item from in infile list 
fastq_in = args.infile[0]

line = True
#execute the code within while loop, while the condition is true
while line:
    lines = []
    #take four lines from the fast1_in at a time 
    for i in range(4):
        line = fastq_in.readline().strip()
        if line:
            lines.append(line)
    #if the lines list is empty stop the while loop
    if not lines: break
    #make a TSV line from four lines in the lines list
    #this corresponds to a single read
    read = '\t'.join(lines)
    #check that the read is the first read type
    #if it is, write it out to the file
    if read.split('\t')[0].endswith('1'):
        for item in read.split('\t'):
            args.outfile_one.write('%s\n' % item)  
    #otherwise it must be the second read type 
    #write it out to a different file 
    else:
        for item in read.split('\t'):
            args.outfile_two.write('%s\n' % item)
