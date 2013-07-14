from helpers.configuration_helper import GetConfigurationsFilename, GetRelativePathFromConfigurationsDirectory
from helpers.file_helper import CreateFileIfItDoesNotExist
from helpers.filename_helper import GetBaseFilenameWithoutExtension

from Packages import package_manager

from xml.etree.ElementTree import parse, Element, ElementTree, SubElement

import os

class NewProject:
    """ ADD DESCRIPTION HERE """
    category = "new"
    command = "project"
    description = "Create a new PBF Project"
    minimumNumberOfArguments = 1
    
    def run(self, args):
        """ Run the package """
        self.createNewProject(args[0], args[1])
       
    def createNewProject(self, projectPath, editor):
        """ Create a new project """
        tree = self.getXMLTree()
        self.createProjectXML(tree.getroot(), projectPath, editor)
        tree.write(GetConfigurationsFilename("project.xml"))
        
    def getXMLTree(self):
        """  """
        projectFilename = GetConfigurationsFilename("project.xml")
        if os.path.exists(projectFilename):
            return parse(projectFilename)
        else:
            return self.createConfigurationXML()
        
    def createConfigurationXML(self):
        """ Create the Configuration XML """
        projectFilename = GetConfigurationsFilename("project.xml")
        element = Element("projects")
        tree = ElementTree(element)
        tree.write(projectFilename)
        return tree
        
    def createProjectXML(self, projectsElement, projectPath, editor):
        """ Creaete the Project XML """
        projectElement = SubElement(projectsElement, "project")
        pathElement = SubElement(projectElement, "path")
        pathElement.text = GetRelativePathFromConfigurationsDirectory(projectPath)
        nameElement = SubElement(projectElement, "name")
        nameElement.text = GetBaseFilenameWithoutExtension(projectPath)
        editorElement = SubElement(projectElement, "editor")
        editorElement.text = GetRelativePathFromConfigurationsDirectory(editor)
    
    def help(self):
        """ Print Package usage """
        print "Usage: pbf {category} {command} [path/to/project/root] [editor.exe]".format(category=self.category, command=self.command)
        print "Create a new project at the path provided and set it to use the editor provided" 
    
package_manager.RegisterPackage(NewProject)