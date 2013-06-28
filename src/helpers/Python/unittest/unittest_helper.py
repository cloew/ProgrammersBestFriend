from helpers.filename_helper import Capitalize

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
    