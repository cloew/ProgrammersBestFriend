from Packages import package_manager
import templates.template_manager as template_manager

class NewMain:
    """ Creates a new Python Main file """
    category = "new"
    command = "main"
    description = "Create a new Python main file"
    minimumNumberOfArguments = 1
    
    def run(self, args):
        """ Run the Package """
        print "Creating Python main at:", args[0]
        template_manager.CopyTemplate(args[0], "Python/main.py")
    
    def help(self):
        """ Print the Usage of the New Main Package """
        print "Usage: pbf {category} {command} [path/to/main.py]".format(category=self.category, command=self.command)
        print "\tWill create a main.py file at the location given"
    
package_manager.RegisterPackage(NewMain)