from helpers.filename_helper import GetPythonClassnameFromFilename

from Packages import package_manager
import templates.template_manager as template_manager
import os

class NewConsoleController:
    """ Creates a new Console Controller """
    category = "new"
    command = "cns-ctrl"
    description = "Creates a new Pandemic Console Controller"
    
    def run(self, args):
        """ ADD LOGIC TO RUN THE PACKAGE HERE """
        controllerFileName = args[0]
        controllerName = GetPythonClassnameFromFilename(controllerFileName)
        print "Creating Pandemic Console Controller:", controllerName, "at:", controllerFileName
        self.createController(controllerFileName, controllerName)
        
    def createController(self, controllerFileName, controllerName):
        """ Create the controller file """
        template_manager.CopyTemplate(controllerFileName, "Pandemic/console_controller.py", {"%ControllerName%":controllerName})
    
    def help(self):
        """  """
        print "Usage: pbf new cns-ctrl [path/to/controller]"
        print "\tWill create a PBF Package called [name] at the path given"
    
package_manager.RegisterPackage(NewConsoleController)