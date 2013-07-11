from helpers.configuration_helper import GetConfigurationsFilename
from helpers.file_helper import CreateFileIfItDoesNotExist, GetLinesFromFile
from helpers.filename_helper import GetBaseFilenameWithoutExtension, RemoveFileExtension

import os

def GetPythonPackageForFilename(rootDirectory, filename):
    """ Return the Python Package Path for the given filename from the given Python root """
    path = os.path.relpath(filename, rootDirectory)
    path = RemoveFileExtension(path)
    path = path.replace("/", ".")
    return path.replace("\\", ".")
    
def GetPythonImportString(filenameToImportFrom, imports):
    """ Constructs and returns a Python Import Line """
    fromFilename = GetBaseFilenameWithoutExtension(filenameToImportFrom)
    return "from {0} import {1}".format(fromFilename, ", ".join(imports))

def GetPythonRoots():
    """ Return the Python Roots """
    filename = GetPythonRootsConfigurationsFilename()
    lines = GetLinesFromFile(filename)
    return [line.strip() for line in lines]
    
def GetPythonRootsConfigurationsFilename():
    """ Return the Python Roots Configurations Filename """
    filename = GetConfigurationsFilename("python_roots")
    CreateFileIfItDoesNotExist(filename)
    return filename