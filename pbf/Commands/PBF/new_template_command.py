from pbf.Commands import command_manager
from pbf.helpers.file_helper import GetBasename
from pbf.helpers.filename_helper import GetPythonClassnameFromFilename, GetBaseFilenameWithoutExtension, GetPythonPackageRootForFilename
from pbf.templates import template_manager

class NewTemplateCommand:
    """ Command to create a PBF command to copy a template """
    category = "new"
    command = "template-command"
    description = "Creates a command to copy a template file"
    minimumNumberOfArguments = 1
    
    def run(self, args):
        """ Run the command """
        filepath = args[0]
        print "Creating PBF Template Command:", GetPythonClassnameFromFilename(filepath), "at:", filepath
        self.createTemplateCommand(filepath)
        
    def createTemplateCommand(self, filepath):
        """ Create the PBF template command """
        classname = GetPythonClassnameFromFilename(filepath)
        pieces = GetBaseFilenameWithoutExtension(filepath).split("_")
        categoryName = pieces[0]
        commandName = "-".join(pieces[1:])
        packageRoot = GetBasename(GetPythonPackageRootForFilename(filepath))
        
        template_manager.CopyTemplate(filepath, "PBF/template_command.py", {"%CommandClassName%":classname,
                                                                            "%CategoryName%":categoryName,
                                                                            "%CommandName%":commandName,
                                                                            "%CapitalCommandName%":commandName.capitalize(),
                                                                            "%PackageRoot%":packageRoot})
    
    def help(self):
        """ Print Command usage """
        print "Usage: pbf {category} {command} [path/to/template-command]".format(category=self.category, command=self.command)
        print "Creates a command to copy a template file at the given path"
    
command_manager.RegisterCommand(NewTemplateCommand)