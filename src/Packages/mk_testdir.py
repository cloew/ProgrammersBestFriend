import package_manager
import templates.template_manager as template_manager

from Packages.mk_pydir import MakePyDir

import os

class MakePyTestDir:
    """ Makes a Python test Directory """
    category = "mk"
    command = "testdir"
    description = "Makes a Python Test Directory"
    
    def run(self, args):
        """ Create the Python Test Directory """
        print "Creating Python Test Directory:", args[0]
        self.makeTestDirectory(args[0])
        
    def makeTestDirectory(self, dirname):
        """ Make the Test Directory """
        mkPyDir = MakePyDir()
        mkPyDir.makePyDir(dirname)
        template_manager.CopyTemplate(os.path.join(dirname, "suite.py"), "suite.py")
    
    def help(self):
        """ Print the usage of the Make Test Dir """
        print "Usage: pbf mk testdir [path/to/dir]"
        print "\tWill create a Python Test Directory called [name] at the path given"
    
package_manager.RegisterPackage(MakePyTestDir)