from pbf.helpers.file_helper import IsDirectory
from pbf.helpers.XML.xml_helper import SaveEtreeXMLPrettily

from pbf.Commands import command_manager

from xml.etree.ElementTree import parse, SubElement

import os
import pbf.templates.template_manager as template_manager

class SalesforceGenerateCommand:
    """ Generate Salesforce command xml """
    category = "salesforce"
    command = "generate-command"
    description = "Generate default Salesforce Command XML"
    minimumNumberOfArguments = 1
    
    defaultMetadata = {"ApexClass":["*"],
                       "ApexComponent":["*"],
                       "ApexPage":["*"],
                       "ApexTrigger":["*"],
                       "StaticResource":["*"]}
    
    def run(self, args):
        """ Run the command """
        self.generateCommandXML(args[0])
        
    def generateCommandXML(self, destination, metadata=None):
        """ Generate the Command XML at the given destination with the given metadata """
        if metadata is None:
            metadata = SalesforceGenerateCommand.defaultMetadata
        
        if IsDirectory(destination):
            destination = os.path.join(destination, "command.xml")
        
        template_manager.CopyTemplate(destination, "Salesforce/command.xml")
        self.addMetadataElements(destination, metadata)
        
    def addMetadataElements(self, destination, metadata):
        """ Add Metadata XML to the Command.xml file at destination """
        tree = parse(destination)
        commandElement = tree.getroot()
        
        for name in metadata:
            typesElement = SubElement(commandElement, "types")
            for member in metadata[name]:
                membersElement = SubElement(typesElement, "members")
                membersElement.text = member
            namesElement = SubElement(typesElement, "name")
            namesElement.text = name
            
        SaveEtreeXMLPrettily(tree, destination)
    
    def help(self):
        """ Print Command usage """
        print "Usage: pbf {category} {command} [path/to/command.xml]".format(category=self.category, command=self.command)
        print "Generate default Salesforce Command XML"
    
command_manager.RegisterCommand(SalesforceGenerateCommand)