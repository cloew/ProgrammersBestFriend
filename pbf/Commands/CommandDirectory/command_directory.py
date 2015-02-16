
class CommandDirectory:
    """ Represents a PBF Command Directory """
    
    def __init__(self, packagePath):
        """ Initialize the Command Directory """
        self.packagePath = packagePath
        
    def getPythonPackage(self):
        """ Return the Python package Name for the given directory """
        packagePathString = self.packagePath.replace("\\", "/")
        package_paths = packagePathString.split("/")
        if '' in package_paths:
            package_paths.remove('')
        return ".".join(package_paths)