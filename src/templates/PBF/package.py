from Packages import package_manager

class %PackageName%:
    """ ADD DESCRIPTION HERE """
    category = "%CategoryName%"
    command = "%CommandName%"
    description = "" # ADD DESCRIPTION HERE
    
    def run(self, args):
        """ Run the package """
    
    def help(self):
        """ Print Package usage """
        print "Usage: pbf %CategoryName% %CommandName%" # ADD ADITIONAL PACKAGE ARGUMENTS
        print "" # ADD DETAILED DESCRIPTION 
    
package_manager.RegisterPackage(%PackageName%)