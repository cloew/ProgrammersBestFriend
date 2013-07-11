from helpers.configuration_helper import GetConfigurationsDirectory, GetConfigurationsFilename
from helpers.file_helper import AppendLinesToEndOfFile
from helpers.Python.python_helper import GetPythonRootsConfigurationsFilename

from Packages import package_manager

import os

class AddRoot:
    """ ADD DESCRIPTION HERE """
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
        pathToPythonRoot = os.path.relpath(directory, configurationsDirectory)
        AppendLinesToEndOfFile(rootsFile, ["{0}\n".format(pathToPythonRoot)])
    
    def help(self):
        """ Print Package usage """
        print "Usage: pbf {category} {command} [path/to/root]".format(category=self.category, command=self.command)
        print "Adds the Directory provided as a root for a Python Project."
        print "This information can be used by other oackages to generate proper import paths."
    
package_manager.RegisterPackage(AddRoot)