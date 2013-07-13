from helpers.file_helper import AppendLinesToEndOfFile, CreateDirectoryIfItDoesNotExist, GetLinesFromFile
from Packages import package_manager
import templates.template_manager as template_manager

import os

class InstallTabCompletion:
    """ Install the PBF Tab Completion """
    category = "install"
    command = "tab-completion"
    description = "Install the PBF Tab Completion"
    minimumNumberOfArguments = 0
    
    def run(self, args): # Note: currently only tested for Cygwin
        self.installTabCompletion()
    
    def installTabCompletion(self):
        """ Install the PBF Tab Completion """
        completionDirectory = "/etc/bash_completion.d"
        CreateDirectoryIfItDoesNotExist(completionDirectory)
        completionFilename = os.path.join(completionDirectory, "pbf_completion")
        template_manager.CopyTemplate(completionFilename, "PBF/pbf_completion.sh")
        self.tryToAddTabCompletionToProfile()
        
    def tryToAddTabCompletionToProfile(self):
        """ Tries to Source Tab Completion in the profile """
        profile = os.path.join(os.path.expanduser("~"), ".bashrc")
        lines = GetLinesFromFile(profile)
        
        if "source /etc/bash_completion.d/pbf_completion\n" not in lines:
            AppendLinesToEndOfFile(profile, ["\n", "#Source PBF Tab Completion\n", "source /etc/bash_completion.d/pbf_completion\n"])
            print "PBF Tab Completion will now be sourced by {0}".format(profile)
            print "Please source {0} to have PBF tab-completion in the current shell".format(profile)
        else:
            print "PBF Tab Completion is already sourced from {0}".format(profile)
    
    def help(self):
        """ Print usage """
        print "Usage: pbf {category} {command}".format(category=self.category, command=self.command)
        print "\tWill install the PBF Tab Completion"
    
package_manager.RegisterPackage(InstallTabCompletion)