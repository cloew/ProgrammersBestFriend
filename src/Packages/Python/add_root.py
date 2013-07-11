from helpers.configuration_helper import GetConfigurationsDirectory
from helpers.file_helper import AppendLinesToEndOfFile

from Packages import package_manager

import os

class AddRoot:
    """ ADD DESCRIPTION HERE """
    category = "add"
    command = "root"
    description = "Adds a Directory as the root of a Python Project"
    minimumNumberOfArguments = 1
    roots_filename = "python_roots"
    
    def run(self, args):
        """ Run the package """
        directory = args[0]
        self.addRoot(directory)
        
    def addRoot(self, directory):
        """ Add Python Root Directory to the roots file """
        configurationsDirectory = GetConfigurationsDirectory() 
        rootsFile = os.path.join(configurationsDirectory, self.roots_filename)
        pathToPythonRoot = os.path.relpath(directory, configurationsDirectory)
        
        self.createRootsFileIfNeeded(rootsFile)
        AppendLinesToEndOfFile(rootsFile, ["{0}\n".format(pathToPythonRoot)])
        
    def createRootsFileIfNeeded(self, rootsFile):
        """ Create the Roots File if it does not exist """
        if not os.path.exists(rootsFile):
            with open(rootsFile, 'w'):
                pass
    
    def help(self):
        """ Print Package usage """
        print "Usage: pbf {category} {command} [path/to/root]".format(category=self.category, command=self.command)
        print "Adds the Directory provided as a root for a Python Project."
        print "This information can be used by other oackages to generate proper import paths."
    
package_manager.RegisterPackage(AddRoot)