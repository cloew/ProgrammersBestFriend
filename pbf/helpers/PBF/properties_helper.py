
def GetRequestedPacakges(propertiesFilename=None):
    """ Get the Requested packages for the current working directory """
    requestedPackages = []
    if propertiesFilename is None:
        propertiesFilename = FindPBFProperties()
    
    try:
        with open(propertiesFilename, 'r') as propertyFile:
            requestedPackages = [line.strip() for line in propertyFile.readlines()]
    except IOError:
        pass # If it doesn't exist we just don't add any extra pacakges
    return requestedPackages
    
    
def FindPBFProperties():
    """ Return the current PBF Properties file """
    return '.pbf-properties'