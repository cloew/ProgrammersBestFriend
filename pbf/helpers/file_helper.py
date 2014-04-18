import os

def IsDirectory(filename):
    """ Return if the given filename is a directory """
    return os.path.isdir(filename)

def GetLinesFromFile(filename):
    """ Return Lines from a file """
    lines = []
    with open(filename, 'r') as file:
        lines = file.readlines()
    return lines

def AppendLinesToEndOfFile(filename, lines):
    """ Append the given lines to the end of the file """
    originalLines = GetLinesFromFile(filename)
    allLines = originalLines + lines
    Save(filename, allLines)

def Save(filename, lines=[]):
    """ Writes the given lines to the file specified at the filename """
    with open(filename, 'w') as file:
        file.writelines(lines)

def CreateDirectoryIfItDoesNotExist(directoryName):
    """ Creates the given directory if it does not exist """
    if not IsDirectory(directoryName):
        os.mkdir(directoryName)
        
def CreateFileIfItDoesNotExist(filename):
    """ Creates the given file if it does not exist """
    if not os.path.exists(filename):
        with open(filename, 'w'):
            pass
            
def IsParentDirectory(parent=None, child=None):
    """ Returns if the 1st argument is a parent direectory of the second """
    parentAbsolutePath = os.path.abspath(parent)
    childAbsolutePath = os.path.abspath(child)
    return childAbsolutePath.startswith(parentAbsolutePath)