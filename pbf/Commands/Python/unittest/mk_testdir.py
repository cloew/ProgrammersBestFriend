from pbf.helpers.Python.unittest.unittest_helper import TryToAddSuiteToParent
from pbf.Commands import command_manager
import pbf.templates.template_manager as template_manager

from pbf.Commands.Python.mk_pydir import MakePyDir

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
        suiteFilename = os.path.join(testDirectory, "suite.py")
        template_manager.CopyTemplate(suiteFilename, "Python/unittest/suite.py")
        TryToAddSuiteToParent(suiteFilename)
    
    def help(self):
        """ Print the usage of the Make Test Dir """
        print "Usage: pbf {category} {command} [path/to/dir]".format(category=self.category, command=self.command)
        print "\tWill create a Python Test Directory called Test at the path given"
    
command_manager.RegisterCommand(MakePyTestDir)