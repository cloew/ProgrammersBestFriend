from pbf.helpers.filename_helper import GetPythonClassnameFromFilename
from pbf.Commands import command_manager
import pbf.templates.template_manager as template_manager

class NewClass:
    """ Command to create a new Python class """
    category = "new"
    command = "class"
    description = "Create a new Python Class"
    minimumNumberOfArguments = 1
    
    def run(self, args):
        """ Run the command """
        self.createClass(args[0])
        
    def createClass(self, filename):
        """ Create a Class """
        classname = GetPythonClassnameFromFilename(filename)
        template_manager.CopyTemplate(filename, "Python/class.py", {"%ClassName%":classname})
    
    def help(self):
        """ Print Command usage """
        print "Usage: pbf {category} {command} [path/to/class]".format(category=self.category, command=self.command)
        print "Create a Python class at the path specified"
    
command_manager.RegisterCommand(NewClass)