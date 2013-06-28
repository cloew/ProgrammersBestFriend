from helpers.filename_helper import GetPythonClassnameFromFilename
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
        print "Creating PBF Package:", classname, "at:", args[0]
        template_manager.CopyTemplate(args[0], "PBF/package.py", {"%PackageName%":classname,
                                                                  "%CategoryName%":"",
                                                                  "%CommandName%":""})
    
    def help(self):
        """ Print the Usage of the New Main Package """
        print "Usage: pbf new package [path/to/package]"
        print "\tWill create a PBF Package at the path given"
    
package_manager.RegisterPackage(NewPackage)