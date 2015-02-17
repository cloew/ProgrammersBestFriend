from pbf.helpers.file_helper import Save

import os

class NewPbfProperties:
    """ Command to create new pbf properties file """
    
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