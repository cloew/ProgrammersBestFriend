from pbf.helpers.file_helper import AppendLinesToEndOfFile, CreateDirectoryIfItDoesNotExist, GetLinesFromFile
from pbf.Packages import package_manager
import pbf.templates.template_manager as template_manager

import os

class InstallTabCompletion:
    """ Install the PBF Tab Completion """
    category = "install"
    command = "tab-completion"
    description = "Install the PBF Tab Completion"
    minimumNumberOfArguments = 0
    completionDirectory = "/etc/bash_completion.d"
    completionFilename = "pbf_completion"
    
    def run(self, args): # Note: currently only tested for Cygwin
        self.installTabCompletion()
    
    def installTabCompletion(self):
        """ Install the PBF Tab Completion """
        CreateDirectoryIfItDoesNotExist(self.completionDirectory)
        completionFilename = self.getFullCompletionFilename()
        template_manager.CopyTemplate(completionFilename, "PBF/pbf_completion.sh")
        self.tryToAddTabCompletionToProfile()
        
    def tryToAddTabCompletionToProfile(self):
        """ Tries to Source Tab Completion in the profile """
        profile = os.path.join(os.path.expanduser("~"), ".bashrc")
        lines = GetLinesFromFile(profile)
        sourceCommand = "source {0}".format(self.getFullCompletionFilename())
        sourceLine = "{0}".format(sourceCommand)
        
        if sourceLine not in lines:
            AppendLinesToEndOfFile(profile, ["\n", "#Source PBF Tab Completion\n", sourceLine])
            print "PBF Tab Completion will now be sourced by {0}".format(profile)
            print "Please source {0} to have PBF tab-completion in the current shell".format(profile)
        else:
            print "PBF Tab Completion is already sourced from {0}".format(profile)
    
    def help(self):
        """ Print usage """
        print "Usage: pbf {category} {command}".format(category=self.category, command=self.command)
        print "\tWill install the PBF Tab Completion"
        
    def getFullCompletionFilename(self):
        """ Return the full completion filename """
        return os.path.join(self.completionDirectory, self.completionFilename)
    
package_manager.RegisterPackage(InstallTabCompletion)