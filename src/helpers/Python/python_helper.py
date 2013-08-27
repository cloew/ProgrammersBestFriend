from helpers.configuration_helper import GetConfigurationsFilename, GetRelativePathFromConfigurationsDirectory, GetConfigurationPathRelativeToCurrentDirectory
from helpers.file_helper import CreateFileIfItDoesNotExist, GetLinesFromFile
from helpers.filename_helper import GetBaseFilenameWithoutExtension, RemoveFileExtension

import os

def GetPythonPackageForFilename(rootDirectory, filename):
    """ Return the Python Package Path for the given filename from the given Python root """
    if rootDirectory is not None:
        print "Filename:", filename
        path = os.path.relpath(filename, rootDirectory)
        print "Relative Path:", path
        path = RemoveFileExtension(path)
        path = path.replace("/", ".")
        return path.replace("\\", ".")
    else:
        return GetBaseFilenameWithoutExtension(filename)
    
def GetPythonImportString(filenameToImportFrom, imports, asName=None):
    """ Constructs and returns a Python Import Line """
    packageRoot = GetPythonRootForFilename(filenameToImportFrom)
    print "Package Root:", packageRoot
    package = GetPythonPackageForFilename(packageRoot, filenameToImportFrom)
    print "Package:", package
    asString = ""
    
    if asName is not None and len(imports) == 1:
        asString = " as {0}".format(asName)
    
    importString = "from {0} import {1}{2}\n".format(package, ", ".join(imports), asString)
    return importString

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
            return GetConfigurationPathRelativeToCurrentDirectory(root)
    else:
        return None 