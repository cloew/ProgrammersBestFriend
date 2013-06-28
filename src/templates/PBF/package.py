from Packages import package_manager

class %PackageName%:
    """ ADD DESCRIPTION HERE """
    category = "%CategoryName%"
    command = "%CommandName%"
    description = "" # ADD DESCRIPTION HERE
    minimumNumberOfArguments = 0 # SET MINIMUM NUMBER OF REQUIRED ARGUMENTS
    
    def run(self, args):
        """ Run the package """
    
    def help(self):
        """ Print Package usage """
        print "Usage: pbf {category} {command}".format(category=self.category, command=self.command) # ADD ADITIONAL PACKAGE ARGUMENTS
        print "" # ADD DETAILED DESCRIPTION 
    
package_manager.RegisterPackage(%PackageName%)