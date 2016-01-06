from .insert_pbf_package import InsertPbfPackage
from pbf.helpers.file_helper import Save, GetDirname
from pbf.helpers.PBF.properties_helper import FindPropertyConfigs, GetPropertyConfigurationsFilename

import os

class NewPbfProperties:
    """ Command to create new pbf properties file """
    
    def addArguments(self, parser):
        """ Add arguments to the parser """
        parser.add_argument('destination', action='store', nargs='?', default='.', help='Destination directory to add .pbf-properties file. Defaults to the current directory')
        parser.add_argument('-c', '--config', action='store', default=None, help='The properties configuration to initialize with')
    
    def run(self, arguments):
        """ Run the command """
        print("Creating PBF Properties at:", arguments.destination)
        self.createPropertiesFile(arguments.destination, config=arguments.config)
        
    def createPropertiesFile(self, path, config=None):
        """ Create Properties file at the given path """
        pathToProperties = os.path.join(path, '.pbf-properties')
        Save(pathToProperties)
        
        if config is not None:
            self.addConfiguredPackages(path, config)
        return pathToProperties
        
    def addConfiguredPackages(self, propertiesDirectory, config):
        """ Add Configured packages to the pbf-properties """
        configToPackages = FindPropertyConfigs()
        if config in configToPackages:
            packages = configToPackages[config]
            InsertPbfPackage().insertPBFPackages(packages, startFrom=propertiesDirectory)
        else:
            print("Unknown Properties Configuration - {0}.".format(config))
            print("\nPlease make sure it is defined in {0}".format(GetPropertyConfigurationsFilename()))