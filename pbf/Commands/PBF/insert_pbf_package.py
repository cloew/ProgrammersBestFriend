from pbf.Commands import command_manager

from pbf.helpers.file_helper import Save
from pbf.helpers.PBF.properties_helper import GetRequestedPacakges, FindPBFPropertiesFilename

import os

class InsertPbfPackage:
    """ Insert a PBF Package into the Properties file """
    
    def addArguments(self, parser):
        """ Add arguments to the parser """
        parser.add_argument('package', action='store', help='Package to add to .pbf-properties')
    
    def run(self, arguments):
        """ Run the command """
        package = arguments.package
        print "Inserting package:", package, "into local pbf properties"
        self.insertPBFPackage(package)
    
    def insertPBFPackage(self, package, directoryToSearchFrom=None):
        """ Insert the provided package into the PBF Properties """
        propertiesFilename = FindPBFPropertiesFilename(directoryToSearchFrom)
        packages = GetRequestedPacakges()
        
        packages.append(package)
        Save(propertiesFilename, [package + '\n' for package in packages])