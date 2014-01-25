from pbf.helpers.file_helper import GetLinesFromFile, Save

import os

local_directory = os.path.dirname(__file__)

def CopyTemplate(filepath, templatepath, keywords={}, templates_directory=local_directory):
    """ Copy the given template to the lcoation given """
    lines = GetTemplateFileLinesWithKeywordsReplaced(templatepath, keywords, templates_directory)
    Save(filepath, lines)
    
def GetTemplateFileLinesWithKeywordsReplaced(templatepath, keywords, templates_directory=local_directory):
    """ Return the lines from given template filepath with all keywords properly replaced """
    lines = GetTemplateFileLines(templatepath, templates_directory)
    return ReplaceKeywords(lines, keywords)

def GetTemplateFileLines(templatepath, templates_directory=local_directory):
    """ Return the lines from given template filepath """
    fullTemplatePath = GetRealTemplatePath(templatepath, templates_directory)
    lines = GetLinesFromFile(fullTemplatePath)
    return lines
    
def ReplaceKeywords(lines, keywords):
    """ Replace keywords in the template lines """
    for i in range(len(lines)):
        for keyword in keywords:
            lines[i] = lines[i].replace(keyword, keywords[keyword])
    return lines
    
def GetRealTemplatePath(templatepath, templates_directory=local_directory):
    """ Returns the Actual Path to the template file """
    return os.path.join(templates_directory, templatepath)