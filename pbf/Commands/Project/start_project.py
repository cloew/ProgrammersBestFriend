from pbf.helpers.configuration_helper import GetConfigurationPathRelativeToCurrentDirectory
from pbf.helpers.Project.project_helper import GetParentProjectFromDirectory

from pbf.Commands import command_manager

import os

class StartProject:
    """ Start using a new project """
    category = "start"
    command = "project"
    description = "Start editing a project"
    minimumNumberOfArguments = 0
    
    def run(self, args):
        """ Run the command """
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
            project.start()
    
    def help(self):
        """ Print Command usage """
        print "Usage: pbf {category} {command} [path/to/project/root]".format(category=self.category, command=self.command)
        print "Open the editor for the given project"
    
command_manager.RegisterCommand(StartProject)