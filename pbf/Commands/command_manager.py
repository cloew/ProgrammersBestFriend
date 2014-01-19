from pbf.Commands.Core.command_list import CommandList

RootCommandList = CommandList()

__Commands__ = {}

def RegisterCommand(command, category=None):
    """ Registers a Command with the Command Manager """
    if hasattr(command, "category"):
        category = command.category
        
    commandList = GetCommandListForCategory(category)
    
    commandList.addCommand(command.command, command())
    
def GetCommandListForCategory(category):
    """ Returns the Command List for the given category """
    commandList = RootCommandList
    if category is not None and category != '':
        for category in category.split('/'):
            if category in commandList:
                commandList = commandList[category]
            else:
                newCommandList = CommandList(category)
                commandList.addCommand(category, newCommandList)
                commandList = newCommandList
    return commandList
    
def Run(arguments):
    """ Try to Run the given Command """
    if len(arguments) > 0 and arguments[0] == "-c":
        GetTabCompletion(RootCommandList, arguments[1:])
    else:
        RootCommandList.run(arguments)
        
def GetTabCompletion(rootCommandList, arguments):
    """ Return the tab completion strings """
    results = rootCommandList.getTabCompletion(arguments)
        
    results.sort()
    print " ".join(results)