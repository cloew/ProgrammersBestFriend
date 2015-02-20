from kao_config import GlobalConfigDir
import os

GLOBAL_CONFIG_DIR = '.pbf'

def GetConfigurationsDirectory():
    """ Returns the configurations directory and creates it if it does not exist """
    global GLOBAL_CONFIG_DIR
    return GlobalConfigDir(GLOBAL_CONFIG_DIR, create=True)
   
def GetConfigurationsFilename(filename, create=False):    
    """ Returns the path to a file in the configurations directory """
    return GetConfigurationsDirectory().getFile(filename, create=create)
    
def GetConfigurationPathRelativeToCurrentDirectory(filename):
    """ Return a relative path from the current directory to a path from the configurations directory """
    pathRelativeToConfigurationsDirectory = os.path.join(GetConfigurationsDirectory(), filename)
    return os.path.relpath(pathRelativeToConfigurationsDirectory)
    
def GetRelativePathFromConfigurationsDirectory(filename):
    """ Returns the relative path from the configurations directory to the file given """
    return os.path.relpath(filename, GetConfigurationsDirectory())