from kao_config import GetUserHomeFolder
from pbf.helpers.file_helper import AppendLinesToEndOfFile, CreateDirectoryIfItDoesNotExist, GetLinesFromFile
from pbf.templates.template_loader import TemplateLoader

import os

class InstallTabCompletion:
    """ Install the PBF Tab Completion """
    completionDirectory = "/etc/bash_completion.d"
    TEMPLATE_LOADER = TemplateLoader("PBF/pbf_completion.sh", defaultFilename="pbf_completion")
    
    def addArguments(self, parser):
        """ Add arguments to the parser """
        pass # No Arguments needed
    
    def run(self, arguments): # Note: currently only tested for Cygwin
        self.installTabCompletion()
    
    def installTabCompletion(self):
        """ Install the PBF Tab Completion """
        CreateDirectoryIfItDoesNotExist(self.completionDirectory)
        self.TEMPLATE_LOADER.copy(self.completionDirectory)
        self.tryToAddTabCompletionToProfile()
        
    def tryToAddTabCompletionToProfile(self):
        """ Tries to Source Tab Completion in the profile """
        profile = os.path.join(GetUserHomeFolder(), ".bashrc")
        lines = GetLinesFromFile(profile)
        sourceCommand = "source {0}".format(self.getFullCompletionFilename())
        sourceLine = "{0}".format(sourceCommand)
        
        if sourceLine not in lines:
            AppendLinesToEndOfFile(profile, ["\n", "#Source PBF Tab Completion\n", sourceLine])
            print "PBF Tab Completion will now be sourced by {0}".format(profile)
            print "Please source {0} to have PBF tab-completion in the current shell".format(profile)
        else:
            print "PBF Tab Completion is already sourced from {0}".format(profile)