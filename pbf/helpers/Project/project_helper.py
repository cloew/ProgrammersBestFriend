from pbf.helpers.configuration_helper import GetRelativePathFromConfigurationsDirectory
from pbf.helpers.file_helper import IsParentDirectory
from pbf.helpers.filename_helper import GetBaseFilenameWithoutExtension
from pbf.helpers.Project.project import Project
from pbf.helpers.Project.project_xml_helper import GetProjectXMLTree

import os
    
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