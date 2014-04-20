from pbf.helpers.filename_helper import GetPythonClassnameFromFilename, GetBaseFilenameWithoutExtension
from pbf.Commands import command_manager
import pbf.templates.template_manager as template_manager

import os

class NewCommand:
    """ Creates a new PBF Command file """
    category = "new"
    command = "command"
    description = "Create a new PBF command file"
    minimumNumberOfArguments = 1
    
    def run(self, args):
        """ Run the Command """
        filepath = args[0]
        print "Creating PBF Command:", GetPythonClassnameFromFilename(filepath), "at:", filepath
        self.createNewCommand(filepath)
        
    def createNewCommand(self, filepath):
        """ Create a new command at the filepath provided """
        classname = GetPythonClassnameFromFilename(filepath)
        pieces = GetBaseFilenameWithoutExtension(filepath).split("_")
        categoryName = pieces[0]
        commandName = "-".join(pieces[1:])
        template_manager.CopyTemplate(filepath, "PBF/command.py", {"%CommandClassName%":classname,
                                                                  "%CategoryName%":categoryName,
                                                                  "%CommandName%":commandName})
    
    def help(self):
        """ Print the Usage of the New Main Command """
        print "Usage: pbf {category} {command} [path/to/command]".format(category=self.category, command=self.command)
        print "\tWill create a PBF Command at the path given"
    
command_manager.RegisterCommand(NewCommand)