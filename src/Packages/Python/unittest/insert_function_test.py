from helpers.file_helper import GetLinesFromFile, Save
from helpers.filename_helper import Capitalize
from Packages import package_manager
import templates.template_manager as template_manager

class InsertFunctionTest:
    """ Package to Insert a test class for a function into a pre-existing test file """
    category = "insert"
    command = "test"
    description = "Insert a Python Function Test Class in a pre-existing Python test file"
    minimumNumberOfArguments = 2
    
    def run(self, args):
        """ Run the package """
        functionToTest = args[0]
        testFilename = args[1]
        print "Inserting Python Test for Function:", functionToTest, "in:", testFilename
        self.insertFunctionTestLogic(functionToTest, testFilename)
        
    def insertFunctionTestLogic(self, functionToTest, testFilename):
        """ Insert Function Test Logic """
        originalLines = GetLinesFromFile(testFilename)
        newLines = self.getTemplateLines(functionToTest)
        
        linesRange = range(len(originalLines))
        linesRange.reverse()
        for i in linesRange:
            line = originalLines[i]
            if "suites = [" in line:
                originalLines = self.addSuiteToSuiteList(originalLines, i, functionToTest)
                originalLines[i-2:i-2] = newLines
                break               
            
        Save(testFilename, originalLines)
        
    def getTemplateLines(self, functionToTest):
        """ Return the lines from the template file """
        capitalName = Capitalize(functionToTest)
        return template_manager.GetTemplateFileLinesWithKeywordsReplaced("Python/unittest/functiontest.py", 
                                                                            {"%functionToTest%":functionToTest,
                                                                             "%FunctionToTest%":capitalName})
        
    def addSuiteToSuiteList(self, lines, startingLineNumber, functionToTest):
        """ Add the current suite to the suite List """
        suiteName = "suite"+Capitalize(functionToTest)
        replaceString = ",\n          {0}]".format(suiteName)
        
        if "[]" in lines[startingLineNumber]:
            replaceString = "{0}]".format(suiteName)
            
        for i in range(startingLineNumber, len(lines)):
            line = lines[i]
            if  "]" in line:
                lines[i] = line.replace("]", replaceString)
                return lines
    
    def help(self):
        """ Print the Usage of the Insert Function Test Package """
        print "Usage: pbf {category} {command} [FunctionToTest] [path/to/test]".format(category=self.category, command=self.command)
        print "\tWill create a new unittest style test class for the given function in the file at the path given"
    
package_manager.RegisterPackage(InsertFunctionTest)