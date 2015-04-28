import os

def getListOfFiles(rootDir, fileDir):

    """
    This function loop over a root directory and searches for 
    sub-directories under the root. Sub-directory is specified by
    --fileDir. The function return a list of files from sub-directory,
    i.e from all directories under the root that match --fileDir input.
    """
                
    listOfFiles = []
    
    for root, dirs, files in os.walk(rootDir):
        if dirs:
            if fileDir in dirs:
                test = dirs[dirs.index(fileDir)]
                testDir = os.path.join(root, test)
                if testDir:
                    for i in os.listdir(testDir):
                        if i != ".dir_bash_history":
                            listOfFiles.append(os.path.join(testDir, i))
    return listOfFiles
