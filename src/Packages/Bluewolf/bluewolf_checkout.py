from Packages import package_manager

from helpers.os_helper import RunCommand
from subprocess import Popen, PIPE

class BluewolfCheckout:
    """ Checkout a project from Blueowlf """
    category = "bluewolf"
    command = "checkout"
    description = "Checkout a Client Salesforce Organization"
    minimumNumberOfArguments = 2
    
    svnPath = "https://pl5.projectlocker.com/bluewolf/codeblue/svn"
    svnClientPath = svnPath+"/clients"
    
    def run(self, args):
        """ Run the package """
        requestedClient = args[0]
        requestedType = args[1]
        
        clients = self.getClients()
        client = self.findClient(requestedClient, clients)
        print client
        
        clientOrganizationTypes = self.getClientOrganizationTypes(client)
        print clientOrganizationTypes
        
        type = self.findOrganizationType(requestedType, clientOrganizationTypes)
        print type
        
        if type is None:
            self.displayOrganizationTypeNotFound(requestedType, clientOrganizationTypes)
            
    def getClients(self):
        """ Return the possible clients """
        return self.getOutputList(["svn", "ls", BluewolfCheckout.svnClientPath])
        
    def findClient(self, requestedClient, clients):
        """ Return the requested Client """
        return self.findItem(requestedClient, clients)
        
    def getClientOrganizationTypes(self, client):
        """ Return the Client Organization Types """
        return self.getOutputList(["svn", "ls", BluewolfCheckout.svnClientPath+"/"+client])
        
    def findOrganizationType(self, requestedType, organizationTypes):
        """ Return the Organization Type Directory that matches the requested type """
        return self.findItem(requestedType, organizationTypes)
            
    def displayOrganizationTypeNotFound(self, requestedType, organizationTypes):
        """ Display the possible Organization Types """
        print "Could not find Organization Type:", requestedType
        print "Possible Organization Types are:"
        for type in organizationTypes:
            print "\t{0}".format(type)
            
    def getOutputList(self, commandList):
        """ Return the output as a list split on newlines """
        output = RunCommand(commandList)
        outputList = output.split('\n')
        outputList.remove('')
        return outputList
        
    def findItem(self, requestedItem, items):
        """ Find and return the requested item from the items list """
        for item in items:
            cleanedItem = item.replace('/', '')
            if cleanedItem.lower() in requestedItem.lower():
                return item
        else:
            return None
    
    def help(self):
        """ Print Package usage """
        print "Usage: pbf {category} {command} [client] [org type] [org name]".format(category=self.category, command=self.command)
        print "Checks out a Bluewolf client org from SVN"
    
package_manager.RegisterPackage(BluewolfCheckout)