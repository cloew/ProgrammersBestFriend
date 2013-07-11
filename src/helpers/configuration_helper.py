import os

def GetConfigurationsDirectory():
    """ Returns the configurations directory and creates it if it does not exist """
    configurationsPath = os.path.join(os.path.dirname(__file__), "../configurations")
    if not os.path.isdir(configurationsPath):
        os.mkdir(configurationsPath)
    return configurationsPath
   