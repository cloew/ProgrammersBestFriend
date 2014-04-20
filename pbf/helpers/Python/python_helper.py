from pbf.helpers.file_helper import IsDirectory

import os

def GetPythonPackageRootForFilename(filename):
    """ Returns the Python Package Root that the filename is in or None """
    absolutePathToFilename = os.path.abspath(filename)
    
    currentPath = absolutePathToFilename
    lastDirectory = None
    while True:
        directory = os.path.dirname(currentPath)
        if not IsPythonDirectory(directory):
            return lastDirectory
        lastDirectory = directory
        currentPath = directory
        
def IsPythonDirectory(directory):
    """ Return if the directory is a Python directory """
    initFilePath = os.path.join(directory, "__init__.py")
    return IsDirectory(directory) and os.path.exists(initFilePath)