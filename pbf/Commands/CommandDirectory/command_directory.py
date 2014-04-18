
class CommandDirectory:
    """ Represents a PBF Command Directory """
    
    def __init__(self, packagePath, packageFullPath):
        """ Initialize the Command Directory """
        self.packagePath = packagePath
        self.packageFullPath = packageFullPath
        
    def getPyhtonPackage(self):
        """ Return the Python package Name for the given directory """
        packagePathString = self.packagePath.replace("\\", "/")
        package_paths = packagePathString.split("/")
        if '' in package_paths:
            package_paths.remove('')
        return ".".join(package_paths)