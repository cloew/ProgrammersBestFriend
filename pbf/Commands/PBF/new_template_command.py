from pbf.Commands import command_manager
from pbf.helpers.file_helper import GetBasename
from pbf.helpers.filename_helper import GetPythonClassnameFromFilename, GetPythonPackageRootForFilename
from pbf.helpers.PBF.command_helper import GetCommandClassName, GetCommandCategoryAndCommand
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
        classname = GetCommandClassName(filepath)
        categoryName, commandName = GetCommandCategoryAndCommand(filepath)
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