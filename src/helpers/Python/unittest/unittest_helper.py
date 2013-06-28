from helpers.file_helper import GetLinesFromFile, Save
from helpers.filename_helper import Capitalize, GetBaseFilenameWithoutExtension

import os

def TryToAddSuiteToParent(filename):
    """ Try to add a suite to its parent in the unittest test hierarchy """
    suiteFilename = GetParentTestSuite(filename)
    if suiteFilename is not None:
        suitename = GetSuiteNameForFile(filename)
        AddSuiteToSuiteFile(suitename, suiteFilename)

def GetParentTestSuite(filename):
    """ Return the Parent Test Suite for the given test filename """
    parentDirectory = os.path.dirname(filename)
    testSuite = os.path.join(parentDirectory, "suite.py")
    
    if os.path.exists(testSuite):
        return testSuite
    else:
        return None
        
def AddSuiteToSuiteFile(suitename, parentSuiteFilename):
    """ Add suite to the given file """
    lines = GetLinesFromFile(parentSuiteFilename)
    startingLine = FindSuiteStartingLine(lines)
    lines = AddSuiteToSuiteList(lines, startingLine, suitename)
    Save(parentSuiteFilename, lines)

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
    
def GetSuiteNameForFile(filename):
    """ Returns the suitename for the file given """
    basename = GetBaseFilenameWithoutExtension(filename)
    basename = basename.replace("_test", "")
    return basename + "_suite"