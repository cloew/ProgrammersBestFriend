from pbf.Commands import command_manager

from pbf.helpers.file_helper import Save

import os

class InsertPbfPackage:
    """ Insert a PBF Package into the Properties file """
    category = "insert"
    command = "pbf-package"
    description = "Insert a PBF Package into the Properties file"
    minimumNumberOfArguments = 1
    
    def run(self, args):
        """ Run the command """
        print "Inserting package:", args[0], "into local pbf properties"
        self.insertPBFPackage(args[0])
    
    def insertPBFPackage(self, package):
        """ Insert the provided package into the PBF Properties """
        lines = []
        with open('.pbf-properties', 'r') as file:
            lines = [line.strip() for line in file.readlines()]
        lines.append(package)
        Save('.pbf-properties', lines)
    
    def help(self):
        """ Print Command usage """
        print "Usage: pbf {category} {command} [package]".format(category=self.category, command=self.command)
        print "Insert the provided package into the PBF Properties file"
    
command_manager.RegisterCommand(InsertPbfPackage)