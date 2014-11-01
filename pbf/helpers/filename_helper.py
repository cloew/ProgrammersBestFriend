import os
import re

def GetBaseFilenameWithoutExtension(filename):
    """ Return the base filename without the file extension """
    fullPath = os.path.abspath(filename)
    basename = os.path.basename(fullPath)
    return RemoveFileExtension(basename)

def RemoveFileExtension(filename):
    """ Return the filename without the extension """
    return os.path.splitext(filename)[0]

def GetPythonClassnameFromFilename(filename):
    """ Returns a capitalized camel-case Python name from a Python filename """
    filenameWithoutExtension = GetBaseFilenameWithoutExtension(filename)
    pieces = filenameWithoutExtension.split("_")
    
    className = ""
    for piece in pieces:
        className += piece.capitalize()
    return className
    
def GetFilenameFromClassname(classname):
    """ Returns a underscore separated filename for a capitalized camel-case Class name """
    pieces = re.findall('[A-Z]+[^A-Z]*', classname) # Will not work preoprly for names with mutliple capital letter s together like HTTPHandler
    
    lowerPieces = []
    for piece in pieces:
        lowerPieces.append(piece.lower())
    
    return "_".join(lowerPieces)
    
    className = ""
    for piece in pieces:
        className += Capitalize(piece)
    return className
    
def Capitalize(string):
    """ Capitalizes ONLY the first letter of the given string """
    return string.replace(string[0], string[0].upper(), 1)