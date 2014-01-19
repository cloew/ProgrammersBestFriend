from Packages import package_manager

from helpers.Bluewolf.error_helper import DisplayPossibleOrganizationTypes, DisplayPossibleOrganizations
from helpers.Bluewolf.not_found_exception import NotFoundException
from helpers.Bluewolf.svn_helper import Checkout, FindClient, FindOrganizationTypeForClient, FindOrganizationForClientAndType, GetClientOrganizationTypes, GetClientOrganizations

class BluewolfCheckout:
    """ Checkout a project from Bluewolf """
    category = "bluewolf"
    command = "checkout"
    description = "Checkout a Client Salesforce Organization"
    minimumNumberOfArguments = 1
    
    def run(self, args):
        """ Run the package """
        self.unpackArguments(args)
        
        try:
            if len(args) == 1:
                client = FindClient(self.requestedClient)
                organizationTypes = GetClientOrganizationTypes(client)
                DisplayPossibleOrganizationTypes(organizationTypes)
            elif len(args) == 2:
                client, type = FindOrganizationTypeForClient(self.requestedClient, self.requestedType)
                organizations = GetClientOrganizations(client, type)
                DisplayPossibleOrganizations(organizations)
            else:
                self.checkout(self.requestedClient, self.requestedType, self.requestedOrganization)

        except NotFoundException as exception:
            print exception.message
        
    def checkout(self, requestedClient, requestedType, requestedOrganization):
        """ Checkout the SVN folder for the given client and type if possible """
        client, type, organization = FindOrganizationForClientAndType(requestedClient, requestedType, requestedOrganization)
        
        if client is not None and type is not None and organization is not None:
            Checkout(client, type, organization, "{0}-{1}".format(type.lower().replace('/', ''), organization.lower().replace('/', '')))
                
    def unpackArguments(self, args):
        """ Unpack the arguments """
        self.requestedClient = args[0]
        self.requestedType = ''
        self.requestedOrganization = ''
        
        if len(args) > 1:
            self.requestedType = args[1]
        if len(args) > 2:
            self.requestedOrganization = args[2]
        
                
    def help(self):
        """ Print Package usage """
        print "Usage: pbf {category} {command} [client] [org type] [org name]".format(category=self.category, command=self.command)
        print "Checks out a Bluewolf client org from SVN"
    
package_manager.RegisterPackage(BluewolfCheckout)