import os

def CopyTemplate(filepath, templatepath, keywords={}):
    """ Copy the given template to the lcoation given """
    lines = GetTemplateFileLines(templatepath)
    lines = ReplaceKeywords(lines, keywords)
    Save(filepath, lines)

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
    
def Save(filepath, lines):
    """ Writes the given lines to the file specified at the filepath """
    file = open(filepath, 'w')
    file.writelines(lines)
    file.close()
    
def GetRealTemplatePath(templatepath):
    """ Returns the Actula Path to the template file """
    templates_directory = os.path.dirname(__file__)
    return os.path.join(templates_directory, templatepath)