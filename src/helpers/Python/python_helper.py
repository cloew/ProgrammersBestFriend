from helpers.configuration_helper import GetConfigurationsFilename, GetRelativePathFromConfigurationsDirectory
from helpers.file_helper import CreateFileIfItDoesNotExist, GetLinesFromFile
from helpers.filename_helper import GetBaseFilenameWithoutExtension, RemoveFileExtension

import os

def GetPythonPackageForFilename(rootDirectory, filename):
    """ Return the Python Package Path for the given filename from the given Python root """
    if rootDirectory is not None:
        path = os.path.relpath(filename, rootDirectory)
        path = RemoveFileExtension(path)
        path = path.replace("/", ".")
        return path.replace("\\", ".")
    else:
        return GetBaseFilenameWithoutExtension(filename)
    
def GetPythonImportString(filenameToImportFrom, imports):
    """ Constructs and returns a Python Import Line """
    packageRoot = GetPythonRootForFilename(filenameToImportFrom)
    package = GetPythonPackageForFilename(packageRoot, filenameToImportFrom)
    return "from {0} import {1}".format(package, ", ".join(imports))

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
    
def GetPythonRootForFilename(filename):
    """ Returns the Python Project Root that the filename is in or None """
    roots = GetPythonRoots()
    relativeFilepath = GetRelativePathFromConfigurationsDirectory(filename)
    for root in roots:
        if root in relativeFilepath:
            return os.path.relpath(root)
    else:
        return None 