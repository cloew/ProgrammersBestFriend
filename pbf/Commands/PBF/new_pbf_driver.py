from pbf.Commands import command_manager
from pbf.helpers.file_helper import IsDirectory
from pbf.templates import template_manager

import os

class NewPbfDriver:
    """ Command to create a new PBF Package Driver """
    category = "new"
    command = "pbf-driver"
    description = "Create PBF Package Driver to run a development version of PBF"
    minimumNumberOfArguments = 1
    
    def run(self, args):
        """ Run the command """
        path = args[0]
        package = args[1]
        
        print "Creating PBF Driver at:", path, "for package:", package
        self.createPBFDriver(path, package)
        
    def createPBFDriver(self, path, package):
        """ Create a PBF Driver at the given directory """
        if IsDirectory(path):
            path = os.path.join(path, "pbf_driver.py")
            
        keywords = {"%Package%":package,
                    "%PackagePath%":package.replace('.', '/')}
        template_manager.CopyTemplate(path, "PBF/pbf_driver.py", keywords)
    
    def help(self):
        """ Print Command usage """
        print "Usage: pbf {category} {command} [path/to/driver] [Python Package]".format(category=self.category, command=self.command)
        print "Create a PBF Driver at the path and for the Python Package specified"
    
command_manager.RegisterCommand(NewPbfDriver)