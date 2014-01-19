from helpers.file_helper import IsDirectory
from helpers.XML.xml_helper import SaveEtreeXMLPrettily

from Packages import package_manager

from xml.etree.ElementTree import parse, SubElement

import os
import templates.template_manager as template_manager

class SalesforceGeneratePackage:
    """ Generate Salesforce package xml """
    category = "salesforce"
    command = "generate-package"
    description = "Generate default Salesforce Package XML"
    minimumNumberOfArguments = 1
    
    def run(self, args):
        """ Run the package """
        self.generatePackageXML(args[0], {"ApexClass":"*", "ApexTrigger":"*"})
        
    def generatePackageXML(self, destination, metadata):
        """ Generate the Package XML at the given destination with the given metadata """
        if IsDirectory(destination):
            destination = os.path.join(destination, "package.xml")
        
        template_manager.CopyTemplate(destination, "Salesforce/package.xml")
        self.addMetadataElements(destination, metadata)
        
    def addMetadataElements(self, destination, metadata):
        """ Add Metadata XML to the Package.xml file at destination """
        tree = parse(destination)
        packageElement = tree.getroot()
        
        for name in metadata:
            typesElement = SubElement(packageElement, "types")
            for member in metadata[name]:
                membersElement = SubElement(typesElement, "members")
                membersElement.text = member
            namesElement = SubElement(typesElement, "name")
            namesElement.text = name
            
        SaveEtreeXMLPrettily(tree, destination)
    
    def help(self):
        """ Print Package usage """
        print "Usage: pbf {category} {command} [path/to/package.xml]".format(category=self.category, command=self.command)
        print "Generate default Salesforce Package XML"
    
package_manager.RegisterPackage(SalesforceGeneratePackage)