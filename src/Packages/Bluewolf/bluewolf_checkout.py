from Packages import package_manager

from subprocess import Popen, PIPE

class BluewolfCheckout:
    """ ADD DESCRIPTION HERE """
    category = "bluewolf"
    command = "checkout"
    description = "Checkout a Client Salesforce Organization"
    minimumNumberOfArguments = 2
    
    svnPath = "https://pl5.projectlocker.com/bluewolf/codeblue/svn"
    
    def run(self, args):
        """ Run the package """
        clientOrganizationTypes = self.getClientOrganizationTypes(args[0])
        print clientOrganizationTypes
        type = self.getOrganizationType(args[1], clientOrganizationTypes)
        print type
        
    def getClientOrganizationTypes(self, client):
        """ Return the Client Organization Types """
        process = Popen(["svn", "ls", BluewolfCheckout.svnPath+"/clients/"+client], stdout=PIPE)
        output, errors  = process.communicate()
        organizationTypes = output.split('\n')
        organizationTypes.remove('')
        return organizationTypes
        
    def getOrganizationType(self, requestedType, organizationTypes):
        """ Return the Organization Type Directory that matches the requested type """
        for type in organizationTypes:
            cleanedType = type.replace('/', '')
            if cleanedType.lower() in requestedType.lower():
                return type
        else:
            return None
    
    def help(self):
        """ Print Package usage """
        print "Usage: pbf {category} {command} [client] [org type] [org name]".format(category=self.category, command=self.command) # ADD ADITIONAL PACKAGE ARGUMENTS
        print "Checks out a Bluewolf client org from SVN"
    
package_manager.RegisterPackage(BluewolfCheckout)