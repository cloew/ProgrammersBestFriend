__Packages__ = {}

def RegisterPackage(package):
    """ Registers a Package with the Package Manager """
    if package.category not in __Packages__:
        __Packages__[package.category] = {}
    __Packages__[package.category][package.command] = package