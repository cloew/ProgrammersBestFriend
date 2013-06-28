from helpers.filename_helper import GetPythonClassnameFromFilename

from Packages import package_manager
import templates.template_manager as template_manager

class NewConsoleView:
    """ Creates a new Console View """
    category = "new"
    command = "cns-view"
    description = "Creates a new Pandemic Console View"
    
    def run(self, args):
        """ Create the Console View """
        viewFileName = args[0]
        viewName = GetPythonClassnameFromFilename(viewFileName)
        print "Creating Pandemic Console View:", viewName, "at:", viewFileName
        self.createView(viewFileName, viewName)
        
    def createView(self, viewFileName, viewName):
        """ Create the controller file """
        template_manager.CopyTemplate(viewFileName, "Pandemic/console_view.py", {"%ViewName%":viewName})
    
    def help(self):
        """  """
        print "Usage: pbf {category} {command} [path/to/view]".format(category=self.category, command=self.command)
        print "\tWill create a Pandemic Console View at the path given"
    
package_manager.RegisterPackage(NewConsoleView)