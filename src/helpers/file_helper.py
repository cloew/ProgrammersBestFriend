import os

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