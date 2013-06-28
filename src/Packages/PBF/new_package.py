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
        print "Creating PBF Package:", args[0], "at:", args[1]
        template_manager.CopyTemplate(args[1], "PBF/package.py", {"%PackageName%":args[0]})
    
    def help(self):
        """ Print the Usage of the New Main Package """
        print "Usage: pbf new package [name] [path/to/package]"
        print "\tWill create a PBF Package called [name] at the path given"
    
package_manager.RegisterPackage(NewPackage)