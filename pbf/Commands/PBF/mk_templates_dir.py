from pbf.Commands import command_manager
from pbf.templates import template_manager

import os

class MkTemplatesDir:
    """ Command to make a PBF Templates Directory """
    category = "mk"
    command = "templates-dir"
    description = "Create a PBF Templates Directory"
    minimumNumberOfArguments = 1
    
    def run(self, args):
        """ Run the command """
        directory = args[0]
        
        print "Creating templates directory in:", directory
        self.makeTemplatesDirectory(directory)
        
    def makeTemplatesDirectory(self, directory):
        """ Make the Template Directory in the directory specified """
        directory = os.path.join(directory, 'templates')
        os.mkdir(directory)
        
        initPath = os.path.join(directory, '__init__.py')
        template_manager.CopyTemplate(initPath, "PBF/template_init.py")
    
    def help(self):
        """ Print Command usage """
        print "Usage: pbf {category} {command} [directory]".format(category=self.category, command=self.command)
        print "Makes the PBF templates ditrectory in the directory given"
    
command_manager.RegisterCommand(MkTemplatesDir)