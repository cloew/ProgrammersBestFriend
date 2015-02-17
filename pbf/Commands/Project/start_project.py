from pbf.helpers.configuration_helper import GetConfigurationPathRelativeToCurrentDirectory
from pbf.helpers.Project.project_helper import GetParentProjectFromDirectory

import os

class StartProject:
    """ Start using a new project """
    
    def addArguments(self, parser):
        """ Add arguments to the parser """
        parser.add_argument('projectpath', nargs='?', action='store', default=os.getcwd(), help='Path to project root to open')
    
    def run(self, arguments):
        """ Run the command """
        path = arguments.projectpath
        self.startProject(path)
        
    def startProject(self, projectPath):
        """ Start the Project """
        project = GetParentProjectFromDirectory(projectPath)
        if project is None:
            print "No project:", project
        else:
            project.start()