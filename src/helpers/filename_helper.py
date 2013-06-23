import os

def GetPythonClassnameFromFilename(filename):
    """ Returns a capitalized camel-case Python name from a Python filename """
    basename = os.path.basename(filename)
    filenameWithoutExtension = os.path.splitext(basename)[0]
    pieces = filenameWithoutExtension.split("_")
    
    className = ""
    for piece in pieces:
        className += piece.capitalize()
    return className