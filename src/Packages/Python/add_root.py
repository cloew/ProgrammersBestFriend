from helpers.configuration_helper import GetConfigurationsDirectory, GetConfigurationsFilename
from helpers.file_helper import Save
from helpers.Python.python_helper import GetPythonRoots, GetPythonRootsConfigurationsFilename

from Packages import package_manager

import os

class AddRoot:
    """ Adds a Python Project Root to a configuration file """
    category = "add"
    command = "root"
    description = "Adds a Directory as the root of a Python Project"
    minimumNumberOfArguments = 1
    
    def run(self, args):
        """ Run the package """
        directory = args[0]
        self.addRoot(directory)
        
    def addRoot(self, directory):
        """ Add Python Root Directory to the roots file """
        configurationsDirectory = GetConfigurationsDirectory() 
        rootsFile = GetPythonRootsConfigurationsFilename()
        roots = GetPythonRoots()
        pathToPythonRoot = os.path.relpath(directory, configurationsDirectory)
        
        if pathToPythonRoot not in roots:
            roots.append(pathToPythonRoot)
            Save(rootsFile, ["{0}\n".format(root) for root in roots])
        else:
            print "{0} is already a Python Project root".format(directory)
    
    def help(self):
        """ Print Package usage """
        print "Usage: pbf {category} {command} [path/to/root]".format(category=self.category, command=self.command)
        print "Adds the Directory provided as a root for a Python Project."
        print "This information can be used by other oackages to generate proper import paths."
    
package_manager.RegisterPackage(AddRoot)