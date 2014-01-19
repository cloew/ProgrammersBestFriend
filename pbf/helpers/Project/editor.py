from pbf.helpers.configuration_helper import GetConfigurationPathRelativeToCurrentDirectory

import os

class Editor:
    """ Represents an editor for a pbf project """
    
    def __init__(self, editorElement):
        """ Initialize the Editor """
        self.editorElement = editorElement
        self.arguments = []
        for argumentElement in self.editorElement.find("arguments").findall("argument"):
            self.arguments.append(argumentElement.text)
        
    def start(self):
        """ Start the Editor Command """
        commandString = "{0} {1}".format(self.command, " ".join(self.arguments))
        os.system(commandString)
        
    def open(self, filename):
        """ Open the given file """
        commandString = "{0} {1}".format(self.command, filename)
        os.system(commandString)
        
    @property
    def command(self):
        """ Return the Project Command """
        return GetConfigurationPathRelativeToCurrentDirectory(self.editorElement.find('command').text)