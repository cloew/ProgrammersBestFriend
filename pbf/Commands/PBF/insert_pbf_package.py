from pbf.helpers.file_helper import Save
from pbf.helpers.PBF.properties_helper import GetRequestedPacakges, FindPBFPropertiesFilename

import os

class InsertPbfPackage:
    """ Insert a PBF Package into the Properties file """
    
    def addArguments(self, parser):
        """ Add arguments to the parser """
        parser.add_argument('packages', metavar='package', nargs='+', action='store', help='Package to add to .pbf-properties')
    
    def run(self, arguments):
        """ Run the command """
        packages = arguments.packages
        print "Inserting packages:", ", ".join(packages), "into local pbf properties"
        self.insertPBFPackage(packages)
    
    def insertPBFPackage(self, packages, startFrom=None):
        """ Insert the provided package into the PBF Properties """
        propertiesFilename = FindPBFPropertiesFilename(startFrom=startFrom)
        currPackages = GetRequestedPacakges()
        
        currPackages += (packages)
        Save(propertiesFilename, [package + '\n' for package in currPackages])