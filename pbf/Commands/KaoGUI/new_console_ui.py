from pbf.helpers.filename_helper import RemoveFileExtension, GetPythonClassnameFromFilename

from new_console_controller import NewConsoleController
from new_console_view import NewConsoleView

from pbf.Commands import command_manager
import pbf.templates.template_manager as template_manager

class NewConsoleUI:
    """ Creates a new Console Controller & View """
    category = "new"
    command = "cns-ui"
    description = "Crates a new Console UI controller and view"
    minimumNumberOfArguments = 1
    
    def run(self, args):
        """ ADD LOGIC TO RUN THE PACKAGE HERE """
        filename = RemoveFileExtension(args[0])
        uiName = GetPythonClassnameFromFilename(filename)
        print "Creating Console Controller & View:", uiName
        
        consoleViewCommand = NewConsoleView()
        consoleControllerCommand = NewConsoleController()
        
        consoleViewCommand.createView(filename+"_screen.py", uiName+"Screen")
        consoleControllerCommand.createController(filename+"_controller.py", uiName+"Controller")
    
    def help(self):
        """  """
        print "Usage: pbf {category} {command} [path/to/ui]".format(category=self.category, command=self.command)
        print "\tWill create a Console Controller & View at the path given"
    
command_manager.RegisterCommand(NewConsoleUI)