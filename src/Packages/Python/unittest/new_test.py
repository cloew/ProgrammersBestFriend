from Packages import package_manager
import templates.template_manager as template_manager

class NewTest:
    """ Create a New Python Test """
    category = "new"
    command = "test"
    description = "Creates a new Python unittest file"
    minimumNumberOfArguments = 1
    
    def run(self, args):
        """ Create the Python unittest file """
        print "Creating Python Test:", args[0]
        self.newTest(args[0])
        
    def newTest(self, path):
        """ Create the Python unittest file """
        template_manager.CopyTemplate(path, "Python/unittest/test.py")
    
    def help(self):
        """ Print the Usage of the New Test Package """
        print "Usage: pbf {category} {command} [path/to/test]".format(category=self.category, command=self.command)
        print "\tWill create a new unittest style test file at the path given"
    
package_manager.RegisterPackage(NewTest)