from helpers.file_helper import GetLinesFromFile, Save
from helpers.filename_helper import Capitalize, GetBaseFilenameWithoutExtension

import os

def TryToAddSuiteToParent(filename):
    """ Try to add a suite to its parent in the unittest test hierarchy """
    suiteFilename = GetParentTestSuite(filename)
    if suiteFilename is not None:
        suitename = GetSuiteNameForFile(filename)
        lines = GetLinesFromFile(suiteFilename)
        lines = AddImportToSuiteFile(lines, filename)
        lines = AddSuiteToSuiteFile(lines, suitename)
        Save(suiteFilename, lines)

def GetParentTestSuite(filename):
    """ Return the Parent Test Suite for the given test filename """
    if os.path.basename(filename) == "suite.py":
        testSuite = GetParentSuite(filename)
    else:
        testSuite = GetLocalSuite(filename)
    
    if os.path.exists(testSuite):
        return testSuite
    else:
        return None
        
def GetLocalSuite(filename):
    """ Return the local suite filename """
    parentDirectory = os.path.dirname(filename)
    return os.path.join(parentDirectory, "suite.py")
    
def GetParentSuite(filename):
    """ Return the parent suite name """
    parentDirectory = os.path.dirname(filename)
    parentPath = os.path.join(parentDirectory, "../../Test/suite.py")
    
    if not os.path.exists(parentPath):
        parentPath = os.path.join(parentDirectory, "../../test.py")
    basename = os.path.normpath(parentPath)
    return basename
        
def AddSuiteToSuiteFile(lines, suitename):
    """ Add suite to the given file """
    startingLine = FindSuiteStartingLine(lines)
    return AddSuiteToSuiteList(lines, startingLine, suitename)

def FindSuiteStartingLine(lines):
    """ Returns the line number where the suites are defined """
    linesRange = range(len(lines))
    linesRange.reverse()
    for i in linesRange:
        line = lines[i]
        if "suites = [" in line:
            return i
    return len(lines)
    
def AddSuiteToSuiteList(lines, startingLineNumber, suiteName):
    """ Add the current suite to the suite List """
    replaceString = ",\n          {0}]".format(suiteName)
    
    if "[]" in lines[startingLineNumber]:
        replaceString = "{0}]".format(suiteName)
        
    for i in range(startingLineNumber, len(lines)):
        line = lines[i]
        if  "]" in line:
            lines[i] = line.replace("]", replaceString)
            return lines

def AddImportToSuiteFile(lines, suitename):
    """ Add suite to the given file """
    startingLine = FindImportStartingLine(lines)
    return AddImportToSuiteLines(lines, startingLine, suitename)
            
def FindImportStartingLine(lines):
    """ Returns the line number where the imports are defined """
    linesRange = range(len(lines))
    for i in linesRange:
        line = lines[i]
        if "import unittest" in line:
            return i+2
    return 0
    
def AddImportToSuiteLines(lines, startingLineNumber, filename):
    """ Add the current suite to the suite List """
    importString = "from {0} import suite as {1}\n".format(GetBaseFilenameWithoutExtension(filename), GetSuiteNameForFile(filename))
    lines[startingLineNumber:startingLineNumber] = [importString]
    return lines
    
def GetSuiteNameForFile(filename):
    """ Returns the suitename for the file given """
    if os.path.basename(filename) == "suite.py":
        dirname = os.path.dirname(filename)
        basename = os.path.join(dirname, "../")
        basename = os.path.normpath(basename)
        basename = os.path.abspath(basename)
        basename = os.path.basename(basename)
        basename = basename.lower()
    else:
        basename = GetBaseFilenameWithoutExtension(filename)
        basename = basename.replace("_test", "")
    return basename + "_suite"