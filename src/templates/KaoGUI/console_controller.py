%ViewImport%
from kao_gui.console.console_controller import ConsoleController

class %ControllerName%(ConsoleController):
    """ Controller for a *** """
    
    def __init__(self):
        """ Initialize the *** Controller """
        screen = %ViewName%()
        ConsoleController.__init__(self, screen)