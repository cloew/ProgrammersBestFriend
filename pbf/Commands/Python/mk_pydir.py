from pbf.Commands import command_manager
import pbf.templates.template_manager as template_manager

import os

class MakePyDir:
    """ Make a Python Directory """
    category = "mk"
    command = "pydir"
    description = "Makes a Python Directory"
    
    def addArguments(self, parser):
        """ Add arguments to the parser """
        parser.add_argument('directory', action='store', help='Directory to create as a Python package')
    
    def run(self, arguments):
        """ Create the Python Directory and the __init__.py file """
        directory = arguments.directory
        print "Creating Python Directory:", directory
        self.makePyDir(directory)
        
    def makePyDir(self, dirname):
        """ Create the Python directory """
        os.mkdir(dirname)
        template_manager.Save(os.path.join(dirname, "__init__.py"), [])
    
    def help(self):
        """ Print the usage of the Make Py Dir """
        print "Usage: pbf {category} {command} [path/to/dir]".format(category=self.category, command=self.command)
        print "\tWill create a Python Directory called [name] at the path given"
    
command_manager.RegisterCommand(MakePyDir)