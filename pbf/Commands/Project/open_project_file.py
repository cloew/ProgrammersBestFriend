from pbf.helpers.Project.project_helper import GetParentProjectFromDirectory

from pbf.Commands import command_manager

class OpenProjectFile:
    """ Open a file within the current Project Context """
    category = "project"
    command = "open"
    description = "Open a file within the currrent project"
    minimumNumberOfArguments = 1
    
    def run(self, args):
        """ Run the command """
        project = GetParentProjectFromDirectory()
        filename = args[0]
        print "Opening {0} in project {1}".format(filename, project)
        self.open(filename, project)
        
    def open(self, filename, project):
        """ Open the file for the given project """
        project.open(filename)
    
    def help(self):
        """ Print Command usage """
        print "Usage: pbf {category} {command} [file]".format(category=self.category, command=self.command)
        print "Opne the given file using the project's defined editor"
    
command_manager.RegisterCommand(OpenProjectFile)