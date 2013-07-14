from helpers.configuration_helper import GetConfigurationsFilename, GetRelativePathFromConfigurationsDirectory

from xml.etree.ElementTree import parse, Element, ElementTree

import os

def GetProjectXMLFilename():
    """ Return the Project XML filename """
    return GetConfigurationsFilename("project.xml")

def GetProjectXMLTree():
    """ Return the Project XML Tree """
    projectFilename = GetProjectXMLFilename()
    if os.path.exists(projectFilename):
        return parse(projectFilename)
    else:
        return CreateConfigurationXML()
    
def CreateConfigurationXML():
    """ Create the Configuration XML """
    projectFilename = GetProjectXMLFilename()
    element = Element("projects")
    tree = ElementTree(element)
    tree.write(projectFilename)
    return tree
    
def SaveProjectXML(tree):
    """ Save the Project XML with the given tree """
    tree.write(GetProjectXMLFilename())
    
def HasProjectWithPath(projectPath):
    """ Returns if there is a project with the given path """
    return GetProjectFromPath(projectPath) is not None
    
def GetProjectFromPath(projectPath):
    """ Returns Project XML or None """
    tree = GetProjectXMLTree()
    cleanedPath = GetRelativePathFromConfigurationsDirectory(projectPath)
    
    for projectXML in tree.getroot().findall("project"):
        pathXML = projectXML.find("path")
        if cleanedPath == pathXML.text:
            return projectXML
    else:
        return None
        