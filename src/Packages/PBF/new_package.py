from helpers.filename_helper import GetPythonClassnameFromFilename, GetBaseFilenameWithoutExtension
from Packages import package_manager
import templates.template_manager as template_manager

import os

class NewPackage:
    """ Creates a new PBF Package file """
    category = "new"
    command = "package"
    description = "Create a new PBF package file"
    
    def run(self, args):
        """ Run the Package """
        classname = GetPythonClassnameFromFilename(args[0])
        pieces = GetBaseFilenameWithoutExtension(args[0]).split("_")
        categoryName = pieces[0]
        commandName = "-".join(pieces[1:])
        print "Creating PBF Package:", classname, "at:", args[0]
        template_manager.CopyTemplate(args[0], "PBF/package.py", {"%PackageName%":classname,
                                                                  "%CategoryName%":categoryName,
                                                                  "%CommandName%":commandName})
    
    def help(self):
        """ Print the Usage of the New Main Package """
        print "Usage: pbf {category} {command} [path/to/package]".format(category=self.category, command=self.command)
        print "\tWill create a PBF Package at the path given"
    
package_manager.RegisterPackage(NewPackage)