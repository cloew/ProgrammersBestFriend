from Packages import package_manager
import templates.template_manager as template_manager

import os

class MakePyDir:
    """ Make a Python Directory """
    category = "mk"
    command = "pydir"
    description = "Makes a Python Directory"
    
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
        print "Usage: pbf mk pydir [path/to/dir]"
        print "\tWill create a Python Directory called [name] at the path given"
    
package_manager.RegisterPackage(MakePyDir)