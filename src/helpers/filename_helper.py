import os

def RemoveFileExtension(filename):
    """ Return the filename without the extension """
    return os.path.splitext(filename)[0]

def GetPythonClassnameFromFilename(filename):
    """ Returns a capitalized camel-case Python name from a Python filename """
    basename = os.path.basename(filename)
    filenameWithoutExtension = RemoveFileExtension(basename)
    pieces = filenameWithoutExtension.split("_")
    
    className = ""
    for piece in pieces:
        className += piece.capitalize()
    return className