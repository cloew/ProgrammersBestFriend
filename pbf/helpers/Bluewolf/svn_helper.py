from helpers.os_helper import RunCommand
from helpers.Bluewolf.error_helper import GetClientNotFoundMessage, GetOrganizationTypeNotFoundMessage, GetOrganizationNotFoundMessage
from helpers.Bluewolf.not_found_exception import NotFoundException

from subprocess import call

svnPath = "https://pl5.projectlocker.com/bluewolf/codeblue/svn"
svnClientPath = svnPath+"/clients"

def Checkout(client, organizationType, organization, destination):
    """ Checkout the svn directory to the given destination """
    fullSVNPath = "{0}/{1}/{2}/{3}".format(svnClientPath, client, organizationType, organization)
    call(["svn", "checkout", fullSVNPath, destination])

def GetClients():
    """ Return the possible clients """
    return GetOutputList(["svn", "ls", svnClientPath])
    
def FindClient(requestedClient):
    """ Return the requested Client if it exists """
    clients = GetClients()
    client = FindItem(requestedClient, clients)
    
    if client is None:
        raise NotFoundException(GetClientNotFoundMessage(requestedClient, clients))
    return client
    
def FindOrganizationTypeForClient(requestedClient, requestedType):
    """ Return the requested Client if it exists """
    client = FindClient(requestedClient)
    organizationTypes = GetClientOrganizationTypes(client)
    organizationType = FindOrganizationType(requestedType, organizationTypes)
    
    if organizationType is None:
        raise NotFoundException(GetOrganizationTypeNotFoundMessage(requestedType, organizationTypes))
    return client, organizationType
    
def GetClientOrganizationTypes(client):
    """ Return the Client Organization Types """
    return GetOutputList(["svn", "ls", svnClientPath+"/"+client])
    
def FindOrganizationType(requestedType, organizationTypes):
    """ Return the requested Organization Type if it exists """
    return FindItem(requestedType, organizationTypes)
    
def FindOrganizationForClientAndType(requestedClient, requestedType, requestedOrganization):
    """ Return the requested Client if it exists """
    client, type = FindOrganizationTypeForClient(requestedClient, requestedType)
    organizations = GetClientOrganizations(client, type)
    organization = FindClientOrganziation(requestedOrganization, organizations)
    
    if organization is None:
        raise NotFoundException(GetOrganizationNotFoundMessage(requestedOrganization, organizations))
    return client, type, organization
    
def GetClientOrganizations(client, type):
    """ Return the Client Organizations for the specified type """
    return GetOutputList(["svn", "ls", svnClientPath+'/'+client+'/'+type])
    
def FindClientOrganziation(requestedOrganization, organizations):
    """ Return the requested Organization if it exists """
    return FindItem(requestedOrganization, organizations)
    
def GetOutputList(commandList):
    """ Return the output as a list split on newlines """
    output = RunCommand(commandList)
    outputList = output.split('\n')
    outputList.remove('')
    return outputList
    
def FindItem(requestedItem, items):
    """ Find and return the requested item from the items list """
    for item in items:
        cleanedItem = item.replace('/', '')
        if cleanedItem.lower() == requestedItem.lower():
            return item
    else:
        return None
        