from kao_config import LocalConfigFinder
from pbf.helpers.file_helper import GetDirname
import os

PBF_PROPERTIES_FINDER = None
PROPERTIES_FILENAME = '.pbf-properties'

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
    
    
def FindPBFPropertiesFilename(startFrom=None):
    """ Return the current PBF Properties file """
    global PBF_PROPERTIES_FINDER, PROPERTIES_FILENAME
    
    if PBF_PROPERTIES_FINDER is None:
        PBF_PROPERTIES_FINDER = LocalConfigFinder(PROPERTIES_FILENAME)
    return PBF_PROPERTIES_FINDER.find(startFrom=startFrom)
    
def FindPBFPropertiesDirectory(startFrom=None):
    """ Return the current PBF Properties file """
    global PBF_PROPERTIES_FINDER, PROPERTIES_FILENAME
    
    propertiesFilename = FindPBFPropertiesFilename(startFrom=startFrom)
    return GetDirname(propertiesFilename)