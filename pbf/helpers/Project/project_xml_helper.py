from pbf.helpers.configuration_helper import GetConfigurationsFilename
from pbf.helpers.XML.xml_helper import SaveEtreeXMLPrettily

from xml.etree.ElementTree import parse, Element, ElementTree

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
    SaveEtreeXMLPrettily(__project_xml_tree__, GetProjectXMLFilename())