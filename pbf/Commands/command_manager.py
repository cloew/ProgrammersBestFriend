from pbf.Commands.Core.command_list import CommandList

RootCommandList = CommandList()

class CommandConfig:
    def __init__(self, command, module, description=None):
        """ Initialize the Command Config """
        pieces = command.split(' ', 1)
        if len(pieces) == 1:
            self.command = command
            self.category = None
        else:
            self.category, self.command = pieces
            
        self.module = module
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