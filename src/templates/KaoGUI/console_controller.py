from View.Console.%ViewFilename% import %ViewName%

from kao_gui.console.console_controller import ConsoleController

class %ControllerName%(ConsoleController):
    """ Controller for a *** """
    
    def __init__(self):
        """ Initialize the *** Controller """
        ConsoleController.__init__(self, %ViewName%())