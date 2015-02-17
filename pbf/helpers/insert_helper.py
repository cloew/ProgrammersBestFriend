def AddElementToList(lines, identifier, element):
    """ Add the given element to the identified list in lines """
    startingLineNumber = FindListStartingLine(lines, identifier)
    return InsertElementIntoText(lines, startingLineNumber, element, leadingSpaces=len(identifier))

def FindListStartingLine(lines, identifier):
    """ Returns the line number where the suites are defined """
    linesRange = range(len(lines))
    linesRange.reverse()
    for i in linesRange:
        line = lines[i]
        if identifier in line:
            return i
    return len(lines)
    
def InsertElementIntoText(lines, startingLineNumber, element, leadingSpaces=0):
    """ Insert the current suite to the suite List """
    replaceString = ",\n{0}{1}]".format(" "*leadingSpaces, element)
    
    if "[]" in lines[startingLineNumber]:
        replaceString = "{0}]".format(element)
        
    for i in range(startingLineNumber, len(lines)):
        line = lines[i]
        if  "]" in line:
            lines[i] = line.replace("]", replaceString)
            return lines