from pbf.Commands import command_manager

class NewProject:
    """ Create a New PBF Project     """
    category = "new"
    command = "project"
    description = "Create a new PBF Project"
    
    def addArguments(self, parser):
        """ Add arguments to the parser """
        parser.add_argument('projectroot', action='store', help='Root Directory for the new Project')
        parser.add_argument('editor', nargs='?', action='store', help='Command to use to open projects')
    
    def run(self, arguments):
        """ Run the command """
        self.createNewProject(arguments.projectroot, arguments.editor)
       
    def createNewProject(self, projectPath, editorCommand):
        """ Create a new project """
        from pbf.helpers.Project.project_helper import GetProjectNameFromPath, HasProjectWithPath
        from pbf.helpers.Project.project_xml_helper import GetProjectXMLTree, SaveProjectXML
        
        tree = GetProjectXMLTree()
        if not HasProjectWithPath(projectPath):
            editor = editorCommand.split(' ')[0]
            editorArguments = editorCommand.split(' ')[1:]
            self.createProjectXML(tree.getroot(), projectPath, editor, editorArguments)
            SaveProjectXML()
        else:
            print "A Project for", GetProjectNameFromPath(projectPath), "already exisits"
        
    def createProjectXML(self, projectsElement, projectPath, editor, editorArguments):
        """ Creaete the Project XML """
        from pbf.helpers.configuration_helper import GetRelativePathFromConfigurationsDirectory
        from xml.etree.ElementTree import SubElement
        
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
        """ Print Command usage """
        print "Usage: pbf {category} {command} [path/to/project/root] [editor.exe]".format(category=self.category, command=self.command)
        print "Create a new project at the path provided and set it to use the editor provided" 
    
command_manager.RegisterCommand(NewProject)