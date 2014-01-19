from pbf.Packages import package_manager
import pbf.templates.template_manager as template_manager

import os

class MakePyDir:
    """ Make a Python Directory """
    category = "mk"
    command = "pydir"
    description = "Makes a Python Directory"
    minimumNumberOfArguments = 1
    
    def run(self, args):
        """ Create the Python Directory and the __init__.py file """
        print "Creating Python Directory:", args[0]
        self.makePyDir(args[0])
        
    def makePyDir(self, dirname):
        """ Create the Python directory """
        os.mkdir(dirname)
        template_manager.Save(os.path.join(dirname, "__init__.py"), [])
    
    def help(self):
        """ Print the usage of the Make Py Dir """
        print "Usage: pbf {category} {command} [path/to/dir]".format(category=self.category, command=self.command)
        print "\tWill create a Python Directory called [name] at the path given"
    
package_manager.RegisterPackage(MakePyDir)