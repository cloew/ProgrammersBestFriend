from helpers.configuration_helper import GetConfigurationPathRelativeToCurrentDirectory
from helpers.Project.project_helper import GetParentProjectFromDirectory

from Packages import package_manager

import os

class StartProject:
    """ Start using a new project """
    category = "start"
    command = "project"
    description = "Start editing a project"
    minimumNumberOfArguments = 0
    
    def run(self, args):
        """ Run the package """
        if len(args) == 0:
            projectPath = os.getcwd()
        else:
            projectPath = args[0]
        self.startProject(projectPath)
        
    def startProject(self, projectPath):
        """ Start the Project """
        project = GetParentProjectFromDirectory(projectPath)
        if project is None:
            print "No project:", project
        else:
            editorPath = GetConfigurationPathRelativeToCurrentDirectory(project.editor)
            print "Starting", editorPath
            os.system("{0} -multiInst -nosession {1} &".format(editorPath, GetConfigurationPathRelativeToCurrentDirectory("../helpers/Project/project_helper.py")))
    
    def help(self):
        """ Print Package usage """
        print "Usage: pbf {category} {command} [path/to/project/root]".format(category=self.category, command=self.command)
        print "Open the editor for the given project"
    
package_manager.RegisterPackage(StartProject)