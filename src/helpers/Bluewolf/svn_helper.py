from helpers.os_helper import RunCommand

svnPath = "https://pl5.projectlocker.com/bluewolf/codeblue/svn"
svnClientPath = svnPath+"/clients"

def GetClients():
    """ Return the possible clients """
    return GetOutputList(["svn", "ls", svnClientPath])
    
def FindClient(requestedClient, clients):
    """ Return the requested Client if it exists """
    return FindItem(requestedClient, clients)
    
def GetClientOrganizationTypes(client):
    """ Return the Client Organization Types """
    return GetOutputList(["svn", "ls", svnClientPath+"/"+client])
    
def FindOrganizationType(requestedType, organizationTypes):
    """ Return the requested Organization Type if it exists """
    return FindItem(requestedType, organizationTypes)
    
def GetClientOrganizations(client, type):
    """ Return the Client Organizations for the specified type """
    return GetOutputList(["svn", "ls", svnClientPath+'/'+client+'/'+type])
    
def FindClientOrganziation(requestedOrganization, organizations):
    """ Return the requested Organization if it exists """
    return FindItem(requestedOrganization, organizations)
    
def FindMatchingClients(requestedClient, clients):
    """ Return all matching client names """
    matchingClients = []
    for client in clients:
        if requestedClient.lower() in client.lower():
            matchingClients.append(client)
            
    return matchingClients
    
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