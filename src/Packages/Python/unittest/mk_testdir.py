from Packages import package_manager
import templates.template_manager as template_manager

from Packages.Python.mk_pydir import MakePyDir

import os

class MakePyTestDir:
    """ Makes a Python test Directory """
    category = "mk"
    command = "testdir"
    description = "Makes a Python Test Directory"
    minimumNumberOfArguments = 1
    
    def run(self, args):
        """ Create the Python Test Directory """
        print "Creating Python Test Directory:", args[0]
        self.makeTestDirectory(args[0])
        
    def makeTestDirectory(self, dirname):
        """ Make the Test Directory """
        testDirectory = os.path.join(dirname, "Test")
        mkPyDir = MakePyDir()
        mkPyDir.makePyDir(testDirectory)
        template_manager.CopyTemplate(os.path.join(testDirectory, "suite.py"), "suite.py")
    
    def help(self):
        """ Print the usage of the Make Test Dir """
        print "Usage: pbf {category} {command} [path/to/dir]".format(category=self.category, command=self.command)
        print "\tWill create a Python Test Directory called Test at the path given"
    
package_manager.RegisterPackage(MakePyTestDir)