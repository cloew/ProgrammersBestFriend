from helpers.filename_helper import Capitalize

def FindSuiteStartingLine(lines):
    """ Returns the line number where the suites are defined """
    linesRange = range(len(lines))
    linesRange.reverse()
    for i in linesRange:
        line = lines[i]
        if "suites = [" in line:
            return i
    return len(lines)

def AddSuiteToSuiteList(lines, startingLineNumber, functionToTest):
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
    