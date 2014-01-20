from pbf.Commands import command_manager

class %CommandClassName%:
    """ ADD DESCRIPTION HERE """
    category = "%CategoryName%"
    command = "%CommandName%"
    description = "" # ADD DESCRIPTION HERE
    minimumNumberOfArguments = 0 # SET MINIMUM NUMBER OF REQUIRED ARGUMENTS
    
    def run(self, args):
        """ Run the command """
    
    def help(self):
        """ Print Command usage """
        print "Usage: pbf {category} {command}".format(category=self.category, command=self.command) # ADD ADITIONAL PACKAGE ARGUMENTS
        print "" # ADD DETAILED DESCRIPTION 
    
command_manager.RegisterCommand(%CommandClassName%)