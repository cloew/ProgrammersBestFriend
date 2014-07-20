
class DependencyInjector:
    """ Represents an injector to load modules """
    
    def __init__(self):
        """ Initialize the dependency injector """
        self.modules = {}
        
    def getModules(self, moduleNames):
        """ Return the requested modules """
        self.loadModules(moduleNames)
        return {moduleName:self.modules[moduleName] for moduleName in moduleNames}
        
    def loadModules(self, moduleNames):
        """ Load the given modules """
        for moduleName in moduleNames:
            if moduleName not in self.modules:
                module = __import__(moduleName)
                for piece in moduleName.split('.')[1:]:
                    module = module.__dict__[piece]
                self.modules[moduleName] = module
        
DependencyInjector = DependencyInjector()