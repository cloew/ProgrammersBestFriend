from helpers.configuration_helper import GetRelativePathFromConfigurationsDirectory
from helpers.filename_helper import GetBaseFilenameWithoutExtension
from helpers.Project.project_helper import GetProjectXMLFilename, GetProjectXMLTree, HasProjectWithPath, SaveProjectXML

from Packages import package_manager

from xml.etree.ElementTree import SubElement

class NewProject:
    """ Create a New PBF Project     """
    category = "new"
    command = "project"
    description = "Create a new PBF Project"
    minimumNumberOfArguments = 1
    
    def run(self, args):
        """ Run the package """
        self.createNewProject(args[0], args[1])
       
    def createNewProject(self, projectPath, editor):
        """ Create a new project """
        tree = GetProjectXMLTree()
        if not HasProjectWithPath(projectPath):
            self.createProjectXML(tree.getroot(), projectPath, editor)
            SaveProjectXML(tree)
        else:
            print "A Project for", projectPath, "already exisits"
        
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