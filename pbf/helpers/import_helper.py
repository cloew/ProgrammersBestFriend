
def ImportPythonModule(package, modulename):
    """ Import and return the requested module from the given package """
    module = __import__(package, fromlist=[modulename])
    return getattr(module, modulename)
    
def ImportAndInstantiateClass(packageWithClass):
    """ Import and return the requested module from the given package """
    pieces = packageWithClass.split('.')
    package = ".".join(pieces[:-2])
    modulename = pieces[-2]
    classname = pieces[-1]
    module = ImportPythonModule(package, modulename)
    return getattr(module, classname)()