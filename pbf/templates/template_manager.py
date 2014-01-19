from pbf.helpers.file_helper import GetLinesFromFile, Save

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
    lines = GetLinesFromFile(fullTemplatePath)
    return lines
    
def ReplaceKeywords(lines, keywords):
    """ Replace keywords in the template lines """
    for i in range(len(lines)):
        for keyword in keywords:
            lines[i] = lines[i].replace(keyword, keywords[keyword])
    return lines
    
def GetRealTemplatePath(templatepath):
    """ Returns the Actual Path to the template file """
    templates_directory = os.path.dirname(__file__)
    return os.path.join(templates_directory, templatepath)