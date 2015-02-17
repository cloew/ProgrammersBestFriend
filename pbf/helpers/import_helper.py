
def ImportPythonModule(package, modulename):
    """ Import and return the requested module from the given package """
    module = __import__(package, fromlist=[modulename])
    return getattr(module, modulename)