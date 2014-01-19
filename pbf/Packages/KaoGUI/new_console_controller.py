from helpers.filename_helper import GetPythonClassnameFromFilename, GetFilenameFromClassname
from helpers.Python.python_helper import GetPythonImportString

from Packages import package_manager
import templates.template_manager as template_manager

class NewConsoleController:
    """ Creates a new Console Controller """
    category = "new"
    command = "cns-ctrl"
    description = "Creates a new Console Controller"
    minimumNumberOfArguments = 1
    
    def run(self, args):
        """ ADD LOGIC TO RUN THE PACKAGE HERE """
        controllerFileName = args[0]
        controllerName = GetPythonClassnameFromFilename(controllerFileName)
        print "Creating Console Controller:", controllerName, "at:", controllerFileName
        self.createController(controllerFileName, controllerName)
        
    def createController(self, controllerFileName, controllerName, ):
        """ Create the controller file """
        viewName = controllerName.replace("Controller", "Screen")
        viewFileName = controllerFileName.replace("controller", "screen")
        template_manager.CopyTemplate(controllerFileName, "KaoGUI/console_controller.py", {"%ControllerName%":controllerName,
                                                                                           "%ViewName%":viewName,
                                                                                           "%ViewImport%":GetPythonImportString(viewFileName, [viewName])})
    
    def help(self):
        """  """
        print "Usage: pbf {category} {command} [path/to/controller]".format(category=self.category, command=self.command)
        print "\tWill create a Console Controller at the path given"
    
package_manager.RegisterPackage(NewConsoleController)