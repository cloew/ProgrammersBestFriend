
class PackageList:
    """ Represents a Package that allows access to other Packages """
    minimumNumberOfArguments = 1
    
    def __init__(self, category="PBF"):
        """ Initialize the Package List """
        self.category = category
        self.description = "List of {0} Packages".format(self.category)
        self.packages = {}
        
    def run(self, args):
        """ Run the package list """
        if len(args) > 0 and args[0] in self.packages:
            package = self.packages[args[0]]
            if len(args[1:]) < package.minimumNumberOfArguments:
                package.help()
            else:
                package.run(args[1:])
        else:
            self.help()
        
    def addPackage(self, category, package):
        """ Add the Package to run for the given category """
        self.packages[category] = package
        
    def getCategories(self, arguments):
        """ Return the categories """
        if len(arguments) == 0:
            return self.packages.keys()
        elif arguments[0] in self.packages:
            if hasattr(self.packages[arguments[0]], "getCategories"):
                return self.packages[arguments[0]].getCategories(arguments[1:])
            else:
                return []
        else:
            return []
        
    def help(self):
        """ Print the usage for the Package List """
        print "Available {0} Categories".format(self.category.capitalize())
        for category in self.packages:
            print "    {0:<15}{1}".format(category+":", self.packages[category].description)
            
            
    def __contains__(self, category):
        """ Return whether the Package List has the given category """
        return category in self.packages
        
    def __getitem__(self, key):
        """ Return the package at the given key """
        return self.packages[key]