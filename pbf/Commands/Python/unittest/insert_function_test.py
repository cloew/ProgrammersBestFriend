from pbf.helpers.file_helper import GetLinesFromFile, Save
from pbf.helpers.filename_helper import Capitalize
from pbf.helpers.Python.unittest.unittest_helper import AddSuiteToSuiteList, FindSuiteStartingLine
from pbf.helpers.filename_helper import Capitalize
from pbf.Commands import command_manager
import pbf.templates.template_manager as template_manager

class InsertFunctionTest:
    """ Command to Insert a test class for a function into a pre-existing test file """
    category = "insert"
    command = "test"
    description = "Insert a Python Function Test Class in a pre-existing Python test file"
    minimumNumberOfArguments = 2
    
    def run(self, args):
        """ Run the command """
        functionToTest = args[0]
        testFilename = args[1]
        print "Inserting Python Test for Function:", functionToTest, "in:", testFilename
        self.insertFunctionTestLogic(functionToTest, testFilename)
        
    def insertFunctionTestLogic(self, functionToTest, testFilename):
        """ Insert Function Test Logic """
        originalLines = GetLinesFromFile(testFilename)
        newLines = self.getTemplateLines(functionToTest)
        suiteLineNumber = FindSuiteStartingLine(originalLines)
        
        originalLines = AddSuiteToSuiteList(originalLines, suiteLineNumber, "suite"+Capitalize(functionToTest))
        originalLines[suiteLineNumber-2:suiteLineNumber-2] = newLines
        Save(testFilename, originalLines)
        
    def getTemplateLines(self, functionToTest):
        """ Return the lines from the template file """
        capitalName = Capitalize(functionToTest)
        return template_manager.GetTemplateFileLinesWithKeywordsReplaced("Python/unittest/functiontest.py", 
                                                                            {"%functionToTest%":functionToTest,
                                                                             "%FunctionToTest%":capitalName})
    
    def help(self):
        """ Print the Usage of the Insert Function Test Command """
        print "Usage: pbf {category} {command} [FunctionToTest] [path/to/test]".format(category=self.category, command=self.command)
        print "\tWill create a new unittest style test class for the given function in the file at the path given"
    
command_manager.RegisterCommand(InsertFunctionTest)