import sys, os
from Bio import SeqIO
from Bio import Seq
from Bio.SeqRecord import SeqRecord

class SomeClass:
 @staticmethod
 
 def test(fastaFile):
    outfile = open("example.fa", 'w')
    for i in SeqIO.parse(fastaFile, 'fasta'):
        record = SeqRecord(seq=i.seq, id=i.id, name='', description='')
        SeqIO.write(record, outfile, 'fasta')

 @staticmethod
 def getChromosomeSizes(fastaFile, threshold):

     #chrom =">Chr%s"
     bootstrap = 'length %s, coverage %s'
     for record in SeqIO.parse(fastaFile, 'fasta'):
         #splitID = record.id.split("_")
         #coverage = float(splitID[-3])
         #if coverage > threshold:
         #    name = ''.join((splitID[0], splitID[1]))
         #    length = splitID[3]
         #    coverage = splitID[5]
         #    info = bootstrap % (length, coverage)
         #    seqRecord = SeqRecord(seq=record.seq, id=name, description=info)
         #    #print coverage, record.id
         #    SeqIO.write(seqRecord, sys.stdout, 'fasta')
     
         print '\t'.join([record.id, str(len(record.seq))])
         #print seqRecord.id, len(seqRecord.seq)
         #if seqRecord.id.startswith('NODE_2_length_84994'):

 @staticmethod
 def getListOfFiles(rootDir, fileDir):
 
     listOfFiles = os.listdir(sys.argv[1])
     #"""
     #This function loop over a root directory and searches for 
     #sub-directories under the root. Sub-directory is specified by
     #--fileDir. The function return a list of files from sub-directory,
     #i.e from all directories under the root that match --fileDir input.
     #"""
     #           
     #listOfFiles = []
     #
     #for root, dirs, files in os.walk(rootDir):
     #    if dirs:
     #       if fileDir in dirs:
     #           test = dirs[dirs.index(fileDir)]
     #           testDir = os.path.join(root, test)
     #           if testDir:
     #               for i in os.listdir(testDir):
     #                   if i != ".dir_bash_history":
     #                       listOfFiles.append(os.path.join(testDir, i))
     return listOfFiles
     ##return sys.stdout.write(listOfFiles)

 @staticmethod
 def makeURL(fileDir):
     listOfFiles  =getListOfFilesgt
     rootURL = 'http://localhost:60151/load?file=http'
     host = '3A%2F%2Fbioinformatics.erc.monash.edu'
     filesDits = '2Fhome%%2Fkirill%%2FMichelleMeilak%%2Fbams%%F2%s&genome=mm10&merge=true&name=%s&locus=chrX:56,789,838-56,790,061'
     sample = 'sample-%s'
     #filesDits = "check%%blah%%foo %s"
     
     for i in listOfFiles:
         if i.endswith('bam'):
             #print FilesDits % (i)
             preName = i.strip().split("_")[0]
             name = sample % preName
             igvLink = filesDits % (i, name)
             return '<li>%s <a href="%s">IGV link</a></li>' % (name, '%'.join([rootURL, host, igvLink]))

class OtherClass:
    @staticmethod
    def Uno():
        print("Uno")
