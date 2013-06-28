from Packages import package_manager
import templates.template_manager as template_manager

import os

class InstallTabCompletion:
    """ Install the PBF Tab COmpletion """
    category = "install"
    command = "tab-completion"
    description = "Install the PBF Tab Completion"
    
    def run(self, args): # Note: currently only tested for CYgwin
        """ Install the PBF Tab Completion """
        profile = "/home/FoeDiddly/.bashrc"
        profile = os.path.join(os.path.expanduser("~"), ".bashrc")
        template_manager.CopyTemplate("/etc/bash_completion.d/pbf_completion", "PBF/pbf_completion.sh")
    
        template_manager.AppendLinesToEndOfFile(profile, ["\n", "#Source PBF Tab Completion\n", "source /etc/bash_completion.d/pbf_completion\n"])
    
    def help(self):
        """ Print usage """
        print "Usage: pbf install tab-completion"
        print "\tWill install the PBF Tab Completion"
    
package_manager.RegisterPackage(InstallTabCompletion)