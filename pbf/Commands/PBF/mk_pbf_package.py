from pbf.Commands import command_manager
from pbf.Commands.PBF.new_pbf_properties import NewPbfProperties
from pbf.Commands.PBF.mk_templates_dir import MakeTemplatesDirectory
from pbf.Commands.Python.mk_pydir import MakePyDir
from pbf.helpers.file_helper import CreateDirectoryIfItDoesNotExist

from pbf.templates import template_manager
import os

class MakePBFPackage:
    """ Command to make a new PBF Package """
    category = "mk"
    command = "pbf-package"
    description = "Make a PBF Package directory structure"
    minimumNumberOfArguments = 2
    
    def run(self, args):
        """ Run the command """
        packagePath = args[0]
        packageName = args[1]
        
        print "Making PBF Package at:", packagePath, "for package:", packageName
        self.createNewPackage(packagePath, packageName)
        
    def createNewPackage(self, packagePath, packageName):
        """ Create a new PBF Pacakge """
        CreateDirectoryIfItDoesNotExist(packagePath)
        
        self.createPackageDirectories(packagePath, packageName)
        self.prepareSetupFile(packagePath, packageName)
        
    def createPackageDirectories(self, packagePath, packageName):
        """ Create Pacakge Directories """
        currentDirectory = packagePath
        pythonDirectoryMaker = MakePyDir()
        
        currentDirectory = os.path.join(currentDirectory, packageName)
        pythonDirectoryMaker.makePyDir(currentDirectory)
            
        pythonDirectoryMaker.makePyDir(os.path.join(currentDirectory, "Commands"))
        self.createTemplatesDirectory(currentDirectory)
        
    def createTemplatesDirectory(self, pbfPackageRoot):
        """ Creates the templates Directory in the directory given """
        templateDirectoryMaker = MakeTemplatesDirectory()
        templateDirectoryMaker.makeTemplatesDirectory(pbfPackageRoot)
            
    def prepareSetupFile(self, packagePath, packageName):
        """ Prepares the PBF Package Setup file """
        destination = os.path.join(packagePath, "setup.py")
        keywords = {"%PackagePath%":packageName,
                    "%PackageName%":packageName}
        template_manager.CopyTemplate(destination, "PBF/setup.py", keywords)
    
    def help(self):
        """ Print Command usage """
        print "Usage: pbf {category} {command} [path/to/package] [package name]".format(category=self.category, command=self.command)
        print "Create the PBF Package at the path specified and with the package name given"
    
command_manager.RegisterCommand(MakePBFPackage)