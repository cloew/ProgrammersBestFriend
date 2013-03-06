import os
import sys

def ImportPythonFile(modulename):
    """ Import a Python File """
    if modulename.endswith(".py") and modulename != "__init__.py":
        #print modulename
        try:
            module = __import__("Statements", fromlist=[modulename[:-3]])
            #module = getattr(module, modulename[:-3])
        except ImportError as error:
            print "Couldn't import", modulename
            print error
            continue
    
packagesDirectory = os.path.dirname(__file__)

for modulename in os.listdir(packagesDirectory):
    ImportPythonFile(modulename)