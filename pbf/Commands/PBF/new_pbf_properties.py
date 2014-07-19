from pbf.Commands import command_manager

from pbf.helpers.file_helper import Save

import os

class NewPbfProperties:
    """ COmmand to create new pbf properties file """
    category = "new"
    command = "pbf-properties"
    description = "Creates a new empty PBF Properties file"
    
    def addArguments(self, parser):
        """ Add arguments to the parser """
        parser.add_argument('destination', action='store', help='Destination directory to add .pbf-properties file')
    
    def run(self, arguments):
        """ Run the command """
        print "Creating PBF Properties at:", self.createPropertiesFile(arguments.destination)
        
    def createPropertiesFile(self, path):
        """ Create Properties file at the given path """
        pathToProperties = os.path.join(path, '.pbf-properties')
        Save(pathToProperties)
        return pathToProperties
    
    def help(self):
        """ Print Command usage """
        print "Usage: pbf {category} {command} [path]".format(category=self.category, command=self.command)
        print "Creates a new empty PBF Properties file at the path specified"
    
command_manager.RegisterCommand(NewPbfProperties)