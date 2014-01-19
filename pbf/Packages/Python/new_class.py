from helpers.filename_helper import GetPythonClassnameFromFilename
from Packages import package_manager
import templates.template_manager as template_manager

class NewClass:
    """ Package to create a new Python class """
    category = "new"
    command = "class"
    description = "Create a new Python Class"
    minimumNumberOfArguments = 1
    
    def run(self, args):
        """ Run the package """
        self.createClass(args[0])
        
    def createClass(self, filename):
        """ Create a Class """
        classname = GetPythonClassnameFromFilename(filename)
        template_manager.CopyTemplate(filename, "Python/class.py", {"%ClassName%":classname})
    
    def help(self):
        """ Print Package usage """
        print "Usage: pbf {category} {command} [path/to/class]".format(category=self.category, command=self.command)
        print "Create a Python class at the path specified"
    
package_manager.RegisterPackage(NewClass)