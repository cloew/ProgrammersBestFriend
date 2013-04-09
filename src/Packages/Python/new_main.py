import package_manager
import templates.template_manager as template_manager

class NewMain:
    """ Creates a new Python Main file """
    category = "new"
    command = "main"
    description = "Create a new Python main file"
    
    def run(self, args):
        """ Run the Package """
        print "Creating Python main at:", args[0]
        template_manager.CopyTemplate(args[0], "main.py")
    
    def help(self):
        """ Print the Usage of the New Main Package """
        print "Usage: pbf new main [path/to/main.py]"
        print "\tWill create a main.py file at the location given"
    
package_manager.RegisterPackage(NewMain)