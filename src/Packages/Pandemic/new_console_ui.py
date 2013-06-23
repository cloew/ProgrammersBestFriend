from helpers.filename_helper import RemoveFileExtension, GetPythonClassnameFromFilename

from new_console_controller import NewConsoleController
from new_console_view import NewConsoleView

from Packages import package_manager
import templates.template_manager as template_manager

class NewConsoleUI:
    """ Creates a new Console Controller & View """
    category = "new"
    command = "cns-ui"
    description = "Crates a new Pandemic Console UI controller and view"
    
    def run(self, args):
        """ ADD LOGIC TO RUN THE PACKAGE HERE """
        filename = RemoveFileExtension(args[0])
        uiName = GetPythonClassnameFromFilename(filename)
        print "Creating Pandemic Console Controller & View:", uiName
        
        consoleViewPackage = NewConsoleView()
        consoleControllerPackage = NewConsoleController()
        
        consoleViewPackage.createView(filename+"_view.py", uiName+"View")
        consoleControllerPackage.createController(filename+"_controller.py", uiName+"Controller")
    
    def help(self):
        """  """
        print "Usage: pbf new cns-ui [path/to/ui]"
        print "\tWill create a Pandemic Console COntroller & View at the path given"
    
package_manager.RegisterPackage(NewConsoleUI)