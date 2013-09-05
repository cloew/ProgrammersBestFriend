from helpers.os_helper import GetActionForOS
from Packages import package_manager

from subprocess import call

import os

class Open:
    """ Package to open a given file """
    command = "open"
    description = "Open the provided file in the default editor." # ADD DESCRIPTION HERE
    minimumNumberOfArguments = 1 # SET MINIMUM NUMBER OF REQUIRED ARGUMENTS
    
    def __init__(self):
        """ Initialize the Open package """
        self.osActions = {'cygwin':self.__open_cygwin__,
                          'darwin':self.__open_mac__
                          'win32':self.__open_windows__}
    
    def run(self, args):
        """ Run the package """
        file = args[0]
        print "Opening", file
        self.open(file)
        
    def open(self, file):
        """ Open the given file """
        action = GetActionForOS(self.osActions)
        if action is not None:
            action(file)
        else:
            print "Cannot open a file on this OS."
        
    def __open_cygwin__(self, file):
        """ Open the file on Cygwin """
        call(["cygstart", file])
        
    def __open_windows__(self, file):
        """ Open the file on Windows """
        os.system("START {0}".format(file))
        
    def __open_on_mac__(self, file):
        """ Open the file on Mac """
        call(["open", file])
    
    def help(self):
        """ Print Package usage """
        print "Usage: pbf {command} [file]".format(command=self.command) # ADD ADITIONAL PACKAGE ARGUMENTS
        print "Opens the file provided in the OS's default prgram for the file type" # ADD DETAILED DESCRIPTION 
    
package_manager.RegisterPackage(Open)