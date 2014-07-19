import argparse

class CommandList:
    """ Represents a Command that allows access to other Commands """
    minimumNumberOfArguments = 1
    
    def __init__(self, category="PBF"):
        """ Initialize the Command List """
        self.category = category
        self.description = "List of {0} Commands".format(self.category)
        self.commands = {}
        
    def run(self, args):
        """ Run the command list """
        if len(args) > 0 and args[0] in self.commands:
            command = self.commands[args[0]]
            argsForNextCommand = args[1:]
            if isinstance(command, CommandList):
                command.run(argsForNextCommand)
            else:
                self.runBaseCommand(command, argsForNextCommand)
        else:
            self.help()
            
    def runBaseCommand(self, command, argsForNextCommand):
        """ Run the command with the given arguments """
        parser = self.buildArgParser(command)
        arguments = parser.parse_args(argsForNextCommand)
        command.run(arguments)
        
    def buildArgParser(self, command):
        """ Return a parser """
        parser = argparse.ArgumentParser(prog=self.buildProgramName(command))
        command.addArguments(parser)
        return parser
        
    def buildProgramName(self, command):
        """ Return the program name for the given command """
        programPieces = []
        
        if hasattr(command, 'category'):
            programPieces.append(command.category)
            
        if hasattr(command, 'command'):
            programPieces.append(command.command)
            
        return "pbf {0}".format(" ".join(programPieces))
        
    def addCommand(self, category, command):
        """ Add the Command to run for the given category """
        self.commands[category] = command
        
    def getTabCompletion(self, arguments):
        """ Return the tab completion for the given arguments """
        if len(arguments) == 0:
            return self.commands.keys()
        elif arguments[0] in self.commands:
            if hasattr(self.commands[arguments[0]], "getTabCompletion"):
                return self.commands[arguments[0]].getTabCompletion(arguments[1:])
            else:
                return []
        else:
            return []
        
    def help(self):
        """ Print the usage for the Command List """
        print "Available {0} Categories".format(self.category.capitalize())
        commandList = self.commands.keys()
        commandList.sort()
        for category in commandList:
            print "    {0:<15}{1}".format(category+":", self.commands[category].description)
            
            
    def __contains__(self, category):
        """ Return whether the Command List has the given category """
        return category in self.commands
        
    def __getitem__(self, key):
        """ Return the command at the given key """
        return self.commands[key]