from pbf.Commands import command_manager
from pbf.helpers.filename_helper import GetPythonClassnameFromFilename
from pbf.helpers.PBF.command_helper import GetCommandClassName, GetCommandCategoryAndCommand
import pbf.templates.template_manager as template_manager

import os

class NewCommand:
    """ Creates a new PBF Command file """
    category = "new"
    command = "command"
    description = "Create a new PBF command file"
    
    def addArguments(self, parser):
        """ Add arguments to the parser """
        parser.add_argument('destination', action='store', help='The destination filename to create')
    
    def run(self, arguments):
        """ Run the Command """
        filepath = arguments.destination
        print "Creating PBF Command:", GetPythonClassnameFromFilename(filepath), "at:", filepath
        self.createNewCommand(filepath)
        
    def createNewCommand(self, filepath):
        """ Create a new command at the filepath provided """
        classname = GetCommandClassName(filepath)
        categoryName, commandName = GetCommandCategoryAndCommand(filepath)
        template_manager.CopyTemplate(filepath, "PBF/command.py", {"%CommandClassName%":classname,
                                                                  "%CategoryName%":categoryName,
                                                                  "%CommandName%":commandName})
    
    def help(self):
        """ Print the Usage of the New Main Command """
        print "Usage: pbf {category} {command} [path/to/command]".format(category=self.category, command=self.command)
        print "\tWill create a PBF Command at the path given"
    
command_manager.RegisterCommand(NewCommand)