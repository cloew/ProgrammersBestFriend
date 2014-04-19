import os

PBF_PROPERTIES_DIRECTORY = None

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
    
    
def FindPBFPropertiesFilename():
    """ Return the current PBF Properties file """
    global PBF_PROPERTIES_DIRECTORY
    
    propertiesFilename = None
    if PBF_PROPERTIES_DIRECTORY is None:
        FindPBFPropertiesDirectory()
        
    if PBF_PROPERTIES_DIRECTORY is not None:
        propertiesFilename = os.path.join(PBF_PROPERTIES_DIRECTORY, '.pbf-properties')
    return propertiesFilename
    
def FindPBFPropertiesDirectory():
    """ Return the current PBF Properties file """
    global PBF_PROPERTIES_DIRECTORY
    
    currentDirectory = os.getcwd()
    propertiesFilename = None
    
    while currentDirectory != '/':
        propertiesFilename = os.path.join(currentDirectory, '.pbf-properties')
        if os.path.exists(propertiesFilename):
            PBF_PROPERTIES_DIRECTORY = currentDirectory
            break
        currentDirectory = os.path.dirname(currentDirectory)
    
    return PBF_PROPERTIES_DIRECTORY