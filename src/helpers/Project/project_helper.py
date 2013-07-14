from helpers.configuration_helper import GetConfigurationsFilename

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
    
