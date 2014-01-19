import os

def GetConfigurationsDirectory():
    """ Returns the configurations directory and creates it if it does not exist """
    configurationsPath = os.path.join(os.path.dirname(__file__), "../configurations")
    if not os.path.isdir(configurationsPath):
        os.mkdir(configurationsPath)
    return configurationsPath
   
def GetConfigurationsFilename(filename):    
    """ Returns the path to a file in the configurations directory """
    return os.path.join(GetConfigurationsDirectory(), filename)
    
def GetConfigurationPathRelativeToCurrentDirectory(filename):
    """ Return a relative path from the current directory to a path from the configurations directory """
    pathRelativeToConfigurationsDirectory = os.path.join(GetConfigurationsDirectory(), filename)
    return os.path.relpath(pathRelativeToConfigurationsDirectory)
    
def GetRelativePathFromConfigurationsDirectory(filename):
    """ Returns the relative path from the configurations directory to the file given """
    return os.path.relpath(filename, GetConfigurationsDirectory())