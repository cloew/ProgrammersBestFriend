
class PackageList:
    """ Represents a Package that allows access to other Packages """
    
    def __init__(self, category="PBF"):
        """ Initialize the Package List """
        self.category = category
        self.packages = {}
        
    def run(self, args):
        """ Run the package list """
        if args[0] in self.packages:
            self.packages[args[0]].run(args[1:])
        else:
            self.help()
        
    def addPackage(self, text, package):
        """ Add the Package to run when given text """
        self.packages[text] = package
        
    def help(self):
        """ Print the usage for the Package List """
        print "Available {0.capitalize()} Categories".format(self.category)
        for category in self.packages:
            print "    {0:<15}{1}".format(category+":", self.packages[category].description)