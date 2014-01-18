from Packages import package_manager

from helpers.Bluewolf.svn_helper import GetClients, FindClient, GetClientOrganizationTypes, FindOrganizationType, GetClientOrganizations, FindClientOrganziation, FindMatchingClients

class BluewolfCheckout:
    """ Checkout a project from Blueowlf """
    category = "bluewolf"
    command = "checkout"
    description = "Checkout a Client Salesforce Organization"
    minimumNumberOfArguments = 2
    
    def run(self, args):
        """ Run the package """
        requestedClient = args[0]
        requestedType = args[1]
        requestedOrganization = args[2]
        
        self.checkout(requestedClient, requestedType, requestedOrganization)
        
    def checkout(self, requestedClient, requestedType, requestedOrganization):
        """ Checkout the SVN folder for the given client and type if possible """
        clients = GetClients()
        client = FindClient(requestedClient, clients)
        
        if client is not None:
            clientOrganizationTypes = GetClientOrganizationTypes(client)
            type = FindOrganizationType(requestedType, clientOrganizationTypes)
        
            if type is not None:
                organizations = GetClientOrganizations(client, type)
                organization = FindClientOrganziation(requestedOrganization, organizations)
                if organization is not None:
                    pass
                else:
                    self.displayOrganizationNotFound(requestedOrganization, organizations)
            else:
                self.displayOrganizationTypeNotFound(requestedType, clientOrganizationTypes)
        else:
            self.displayClientNotFound(requestedClient, clients)
        
    def displayClientNotFound(self, requestedClient, clients):
        """ Disaply the possible Clients """
        print "Could not find client:", requestedClient
        print "Did you mean:"
        for client in FindMatchingClients(requestedClient, clients):
            print "\t{0}".format(client)
            
    def displayOrganizationTypeNotFound(self, requestedType, organizationTypes):
        """ Display the possible Organization Types """
        print "Could not find Organization Type:", requestedType
        print "Possible Organization Types are:"
        for type in organizationTypes:
            print "\t{0}".format(type)
            
    def displayOrganizationNotFound(self, requestedOrganization, organizations):
        """ Display the possible Organization Types """
        print "Could not find Organization:", requestedOrganization
        print "Possible Organizations are:"
        for organization in organizations:
            print "\t{0}".format(organization)
                
    def help(self):
        """ Print Package usage """
        print "Usage: pbf {category} {command} [client] [org type] [org name]".format(category=self.category, command=self.command)
        print "Checks out a Bluewolf client org from SVN"
    
package_manager.RegisterPackage(BluewolfCheckout)