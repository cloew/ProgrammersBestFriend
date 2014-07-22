from pbf.Commands import command_manager

class StartProject:
    """ Start using a new project """
    category = "start"
    command = "project"
    description = "Start editing a project"
    
    def addArguments(self, parser):
        """ Add arguments to the parser """
        import os
        parser.add_argument('projectpath', nargs='?', action='store', default=os.getcwd(), help='Path to project root to open')
    
    def run(self, arguments):
        """ Run the command """
        path = arguments.projectpath
        self.startProject(path)
        
    def startProject(self, projectPath):
        """ Start the Project """
        from pbf.helpers.Project.project_helper import GetParentProjectFromDirectory
        
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