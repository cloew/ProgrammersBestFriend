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
        
        self.checkout(requestedClient, requestedType)
        
    def checkout(self, requestedClient, requestedType):
        """ Checkout the SVN folder for the given client and type if possible """
        
        clients = self.getClients()
        client = self.findClient(requestedClient, clients)
        
        if client is not None:
            clientOrganizationTypes = self.getClientOrganizationTypes(client)
            type = self.findOrganizationType(requestedType, clientOrganizationTypes)
        
            if type is None:
                self.displayOrganizationTypeNotFound(requestedType, clientOrganizationTypes)
        else:
            self.displayClientNotFound(requestedClient, clients)
            
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
        
    def displayClientNotFound(self, requestedClient, clients):
        """ Disaply the possible Clients """
        print "Could not find client:", requestedClient
        print "Did you mean:"
        for client in self.findMatchingClients(requestedClient, clients):
            print "\t{0}".format(client)
            
    def displayOrganizationTypeNotFound(self, requestedType, organizationTypes):
        """ Display the possible Organization Types """
        print "Could not find Organization Type:", requestedType
        print "Possible Organization Types are:"
        for type in organizationTypes:
            print "\t{0}".format(type)
            
    def findMatchingClients(self, requestedClient, clients):
        """ Return all matching client names """
        matchingClients = []
        for client in clients:
            if requestedClient.lower() in client.lower():
                matchingClients.append(client)
                
        return matchingClients
            
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
            if cleanedItem.lower() == requestedItem.lower():
                return item
        else:
            return None
    
    def help(self):
        """ Print Package usage """
        print "Usage: pbf {category} {command} [client] [org type] [org name]".format(category=self.category, command=self.command)
        print "Checks out a Bluewolf client org from SVN"
    
package_manager.RegisterPackage(BluewolfCheckout)