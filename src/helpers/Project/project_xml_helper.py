from helpers.configuration_helper import GetConfigurationsFilename

from xml.dom.minidom import parseString
from xml.etree.ElementTree import parse, tostring, Element, ElementTree

import os

__project_xml_tree__ = None

def GetProjectXMLFilename():
    """ Return the Project XML filename """
    return GetConfigurationsFilename("project.xml")

def GetProjectXMLTree():
    """ Return the Project XML Tree """
    global __project_xml_tree__
    projectFilename = GetProjectXMLFilename()
    if __project_xml_tree__ is None:
        if os.path.exists(projectFilename):
            __project_xml_tree__ = parse(projectFilename)
        else:
            __project_xml_tree__ = CreateConfigurationXML()
    return __project_xml_tree__
    
def CreateConfigurationXML():
    """ Create the Configuration XML """
    projectFilename = GetProjectXMLFilename()
    element = Element("projects")
    tree = ElementTree(element)
    tree.write(projectFilename)
    return tree
    
def SaveProjectXML():
    """ Save the Project XML with the given tree """
    xmlString = tostring(__project_xml_tree__.getroot())
    xml = parseString(xmlString)
    prettyXMLString = xml.toprettyxml()
    with open(GetProjectXMLFilename(), 'w') as file:
        file.write(prettyXMLString)