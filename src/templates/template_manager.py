import os

def CopyTemplate(filepath, templatepath, keywords={}):
    """ Copy the given template to the lcoation given """
    lines = GetTemplateFileLinesWithKeywordsReplaced(templatepath, keywords)
    Save(filepath, lines)
    
def GetTemplateFileLinesWithKeywordsReplaced(templatepath, keywords):
    """ Return the lines from given template filepath with all keywords properly replaced """
    lines = GetTemplateFileLines(templatepath)
    return ReplaceKeywords(lines, keywords)

def GetTemplateFileLines(templatepath):
    """ Return the lines from given template filepath """
    fullTemplatePath = GetRealTemplatePath(templatepath)
    file = open(fullTemplatePath, 'r')
    lines = file.readlines()
    file.close()
    return lines
    
def ReplaceKeywords(lines, keywords):
    """ Replace keywords in the template lines """
    for i in range(len(lines)):
        for keyword in keywords:
            lines[i] = lines[i].replace(keyword, keywords[keyword])
    return lines
    
def AppendLinesToEndOfFile(filename, lines):
    """ Append the given lines to the end of the file """
    originalLines = []
    with open(filename, 'r') as file:
        originalLines = file.readlines()
    
    allLines = originalLines + lines
    with open(filename, 'w') as file:
        file.writelines(allLines)
    
def Save(filepath, lines):
    """ Writes the given lines to the file specified at the filepath """
    file = open(filepath, 'w')
    file.writelines(lines)
    file.close()
    
def GetRealTemplatePath(templatepath):
    """ Returns the Actula Path to the template file """
    templates_directory = os.path.dirname(__file__)
    return os.path.join(templates_directory, templatepath)