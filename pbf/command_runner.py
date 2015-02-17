from pbf.Commands import command_manager

def Run(arguments):
    """ Try to Run the given Command """
    if len(arguments) > 0 and arguments[0] == "-c":
        GetTabCompletion(command_manager.RootCommandList, arguments[1:])
    else:
        command_manager.RootCommandList.run(arguments)
        
def GetTabCompletion(rootCommandList, arguments):
    """ Return the tab completion strings """
    results = rootCommandList.getTabCompletion(arguments)
        
    results.sort()
    print " ".join(results)