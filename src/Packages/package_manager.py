__Packages__ = {}

def RegisterPackage(package):
    """ Registers a Package with the Package Manager """
    if package.category not in __Packages__:
        __Packages__[package.category] = {}
    __Packages__[package.category][package.command] = package
    
def Run(arguments):
    """ Try to Run the given Package """
    if len(arguments) == 0:
        PrintCategories()
    else:
        RunCategory(arguments[0], arguments[1:])
        
def RunCategory(category, arguments):
    """ Run the category """
    if category not in __Packages__:
        print "No such Package Category: {0}".format(category)
        PrintCategories()
    elif len(arguments) == 0:
        PrintCommands(category)
    else:
        RunCommand(category, arguments[0], arguments[1:])
        
def RunCommand(category, command, arguments):
    """ Run the specified command """
    if command not in __Packages__[category]:
        print "No such Package Command: {0} for category {1}".format(command, category)
        PrintCommands()
    elif len(arguments) == 0:
        package = GetPackage(category, command)
        package.help()
    else:
        package = GetPackage(category, command)
        package.run(arguments)
        
def GetPackage(category, command):
    """ Return an instance of the Package Class """
    return __Packages__[category][command]()
    
def PrintCategories():
    """ Print the Command Categories """
    PrintUsage()
    print "Available Categories"
    for key in __Packages__:
        print "\t{0}".format(key)
    print "\nFor more information on available commands for each category run: pbf [category]"
    
def PrintCommands(category):
    """  Print the commands for the given category """
    PrintUsage()
    print "Available Commands for Package Category: {0}".format(category)
    for key in __Packages__[category]:
        print "\t{0}".format(key)
    print "\nFor more information on specific arguments for each command run: pbf [category] [command]"
    
def PrintUsage():
    """ Prints the usage for pbf """
    print "Usage: pbf [category] [command] [arguments]"