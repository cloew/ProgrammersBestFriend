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
        classname = GetPythonClassnameFromFilename(args[0])
        pieces = GetBaseFilenameWithoutExtension(args[0]).split("_")
        categoryName = pieces[0]
        commandName = "-".join(pieces[1:])
        print "Creating PBF Command:", classname, "at:", args[0]
        template_manager.CopyTemplate(args[0], "PBF/command.py", {"%CommandClassName%":classname,
                                                                  "%CategoryName%":categoryName,
                                                                  "%CommandName%":commandName})
    
    def help(self):
        """ Print the Usage of the New Main Command """
        print "Usage: pbf {category} {command} [path/to/command]".format(category=self.category, command=self.command)
        print "\tWill create a PBF Command at the path given"
    
command_manager.RegisterCommand(NewCommand)