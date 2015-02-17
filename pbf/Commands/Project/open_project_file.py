from pbf.helpers.Project.project_helper import GetParentProjectFromDirectory

class OpenProjectFile:
    """ Open a file within the current Project Context """
    
    def addArguments(self, parser):
        """ Add arguments to the parser """
        parser.add_argument('filename', action='store', help='File to open')
    
    def run(self, arguments):
        """ Run the command """
        filename = arguments.filename
        project = GetParentProjectFromDirectory()
        print "Opening {0} in project {1}".format(filename, project)
        self.open(filename, project)
        
    def open(self, filename, project):
        """ Open the file for the given project """
        project.open(filename)