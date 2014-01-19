from pbf.helpers.Python.unittest.unittest_helper import TryToAddSuiteToParent
from pbf.Commands import command_manager
from pbf.Commands.Python.unittest.insert_function_test import InsertFunctionTest
import pbf.templates.template_manager as template_manager

class NewTest:
    """ Create a New Python Test """
    category = "new"
    command = "test"
    description = "Creates a new Python unittest file"
    minimumNumberOfArguments = 1
    
    def __init__(self):
        """ Initialize the New Test Command """
        self.insertFunctionTestCommand = InsertFunctionTest()
    
    def run(self, args):
        """ Create the Python unittest file """
        print "Creating Python Test:", args[0]
        self.newTest(args[0])
        
    def newTest(self, path, addTest=True):
        """ Create the Python unittest file """
        template_manager.CopyTemplate(path, "Python/unittest/test.py")
        
        if addTest:
            self.insertFunctionTestCommand.insertFunctionTestLogic("functionToTest", path)
            
        TryToAddSuiteToParent(path)
    
    def help(self):
        """ Print the Usage of the New Test Command """
        print "Usage: pbf {category} {command} [path/to/test]".format(category=self.category, command=self.command)
        print "\tWill create a new unittest style test file at the path given"
    
command_manager.RegisterCommand(NewTest)