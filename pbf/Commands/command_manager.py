from pbf.Commands.Core.command_list import CommandList

RootCommandList = CommandList()

class CommandConfig:
    def __init__(self, command, module, category=None, description=None):
        """ Initialize the Command Config """
        self.command = command
        self.module = module
        self.category = category
        self.description = description
        
def RegisterCommands(commandConfigs):
    """ Register all the given commands with the command manager """
    [RegisterCommand(command) for command in commandConfigs]

def RegisterCommand(commandConfig):
    """ Registers a Command with the Command Manager """
    commandList = GetCommandListForCategory(commandConfig.category)
    commandList.addCommand(commandConfig.command, commandConfig)
    
def GetCommandListForCategory(category):
    """ Returns the Command List for the given category """
    global RootCommandList
    
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