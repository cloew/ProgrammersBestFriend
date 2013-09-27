from helpers.configuration_helper import GetRelativePathFromConfigurationsDirectory
from helpers.Project.project_helper import GetProjectNameFromPath, GetProjectXMLFilename, GetProjectXMLTree, HasProjectWithPath, SaveProjectXML

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
        self.createNewProject(args[0], args[1], args[2:])
       
    def createNewProject(self, projectPath, editor, editorArguments):
        """ Create a new project """
        tree = GetProjectXMLTree()
        if not HasProjectWithPath(projectPath):
            self.createProjectXML(tree.getroot(), projectPath, editor, editorArguments)
            SaveProjectXML()
        else:
            print "A Project for", GetProjectNameFromPath(projectPath), "already exisits"
        
    def createProjectXML(self, projectsElement, projectPath, editor, editorArguments):
        """ Creaete the Project XML """
        projectElement = SubElement(projectsElement, "project")
        pathElement = SubElement(projectElement, "path")
        pathElement.text = GetRelativePathFromConfigurationsDirectory(projectPath)
        nameElement = SubElement(projectElement, "name")
        nameElement.text = GetProjectNameFromPath(projectPath)
        editorElement = SubElement(projectElement, "editor")
        editorCommandElement = SubElement(editorElement, "command")
        editorCommandElement.text = GetRelativePathFromConfigurationsDirectory(editor)
        editorArgumentsElement = SubElement(editorElement, "arguments")
        recentFilesElement = SubElement(projectElement, "recent_files")
        
        for argument in editorArguments:
            editorArgumentElement = SubElement(editorArgumentsElement, "argument")
            editorArgumentElement.text = argument
    
    def help(self):
        """ Print Package usage """
        print "Usage: pbf {category} {command} [path/to/project/root] [editor.exe]".format(category=self.category, command=self.command)
        print "Create a new project at the path provided and set it to use the editor provided" 
    
package_manager.RegisterPackage(NewProject)