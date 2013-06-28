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

def Save(filename, lines):
    """ Writes the given lines to the file specified at the filename """
    with open(filename, 'w') as file:
        file.writelines(lines)