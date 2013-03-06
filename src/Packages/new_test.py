import package_manager
import templates.template_manager as template_manager

class NewTest:
    """ Create a New Python Test """
    category = "new"
    command = "test"
    description = "Creates a new Python unittest file"
    
    def run(self, args):
        """ Create the Python unittest file """
        print "Creating Python Test:", args[0]
        self.newTest(args[0])
        
    def newTest(self, path):
        """ Create the Python unittest file """
        template_manager.CopyTemplate(path, "test.py")
    
    def help(self):
        """ Print the Usage of the New Test Package """
        print "Usage: pbf new test [path/to/test]"
        print "\tWill create a new unittest style test file at the path given"
    
package_manager.RegisterPackage(NewTest)