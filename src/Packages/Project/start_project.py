from helpers.configuration_helper import GetConfigurationPathRelativeToCurrentDirectory
from helpers.Project.project_helper import GetProjectFromPath

from Packages import package_manager

import subprocess
import os

class StartProject:
    """ Start using a new project """
    category = "start"
    command = "project"
    description = "Start editing a project"
    minimumNumberOfArguments = 1
    
    def run(self, args):
        """ Run the package """
        self.startProject(args[0])
        
    def startProject(self, project):
        """ Start the Project """
        projectElement = GetProjectFromPath(project)
        if projectElement is None:
            print "No project:", project
        else:
            editorElement = projectElement.find("editor")
            editor = editorElement.text
            editorPath = GetConfigurationPathRelativeToCurrentDirectory(editor)
            print "Starting", editorPath
            os.system("{0} -multiInst &".format(editorPath))
    
    def help(self):
        """ Print Package usage """
        print "Usage: pbf {category} {command} [path/to/project/root]".format(category=self.category, command=self.command)
        print "Open the editor for the given project"
    
package_manager.RegisterPackage(StartProject)