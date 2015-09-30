from kao_config import LocalConfigFile
from pbf.helpers.configuration_helper import GetConfigurationsFilename
from pbf.helpers.file_helper import GetDirname
import os

PBF_PROPERTIES_FINDER = None
PROPERTIES_FILENAME = '.pbf-properties'
GLOBAL_PROPERTIES_CONFIGS = 'property_configs'

def GetRequestedPacakges():
    """ Get the Requested packages for the current working directory """
    requestedPackages = []
    propertiesFilename = FindPBFPropertiesFilename()
    
    if propertiesFilename is not None:
        try:
            with open(propertiesFilename, 'r') as propertyFile:
                requestedPackages = [line.strip() for line in propertyFile.readlines()]
        except IOError:
            pass # If it doesn't exist we just don't add any extra pacakges
    return requestedPackages
    
    
def FindPBFPropertiesFilename(startFrom=None, reload=False):
    """ Return the current PBF Properties file """
    global PBF_PROPERTIES_FINDER, PROPERTIES_FILENAME
    
    if PBF_PROPERTIES_FINDER is None:
        PBF_PROPERTIES_FINDER = LocalConfigFile(PROPERTIES_FILENAME, startFrom=startFrom)
    return PBF_PROPERTIES_FINDER.path
    
def FindPBFPropertiesDirectory(startFrom=None):
    """ Return the current PBF Properties file """
    global PBF_PROPERTIES_FINDER, PROPERTIES_FILENAME
    
    propertiesFilename = FindPBFPropertiesFilename(startFrom=startFrom)
    return GetDirname(propertiesFilename)
    
def GetPropertyConfigurationsFilename():
    """ Return the Property COnfigurations Filename """
    global GLOBAL_PROPERTIES_CONFIGS
    return GetConfigurationsFilename(GLOBAL_PROPERTIES_CONFIGS, create=True)
    
def FindPropertyConfigs():
    """ Load the global pbf properties configurations """
    filename = GetPropertyConfigurationsFilename()
    
    lines = []
    configs = {}
    with open(filename, 'r') as file:
        lines = file.readlines()
        
    for line in lines:
        configName, packages = line.split(':')
        packages = packages.split(' ')
        packages.remove('')
        configs[configName] = packages
        
    return configs