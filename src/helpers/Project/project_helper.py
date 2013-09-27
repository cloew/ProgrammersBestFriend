from helpers.configuration_helper import GetConfigurationsFilename, GetRelativePathFromConfigurationsDirectory
from helpers.file_helper import IsParentDirectory
from helpers.filename_helper import GetBaseFilenameWithoutExtension
from helpers.Project.project import Project

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
    __project_xml_tree__.write(GetProjectXMLFilename())
    
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
            return Project(projectXML)
    else:
        return None
        
def GetParentProjectFromDirectory(directory=os.getcwd()):
    """ Returns the project that is the parent to the given directory """
    tree = GetProjectXMLTree()
    cleanedPath = GetRelativePathFromConfigurationsDirectory(directory)
    
    for projectXML in tree.getroot().findall("project"):
        pathXML = projectXML.find("path")
        if IsParentDirectory(parent=pathXML.text, child=cleanedPath):
            return Project(projectXML)
    else:
        return None
        
def GetProjectNameFromPath(projectPath):
    """ Returns the Project Name from its path """
    return GetBaseFilenameWithoutExtension(projectPath)