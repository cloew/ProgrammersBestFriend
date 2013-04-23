from Packages import package_manager

class NewPySideMain:
    """ ADD DESCRIPTION HERE """
    category = "new"
    command = "ps_main"
    description = "Create a new PySide Main File"
    
    def run(self, args):
        """ ADD LOGIC TO RUN THE PACKAGE HERE """
        print "Creating PySide main at:", args[0]
        template_manager.CopyTemplate(args[0], "pyside_main.py")
    
    def help(self):
        """ ADD USAGE HERE """
        print "Usage: pbf new ps_main [path/to/main.py]"
        print "\tWill create a main.py file at the location given"
    
package_manager.RegisterPackage(NewPySideMain)