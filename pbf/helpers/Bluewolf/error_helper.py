
def DisplayClientNotFound(requestedClient, clients):
    """ Disaply the possible Clients """
    print GetClientNotFoundMessage(requestedClient, clients)
        
def GetClientNotFoundMessage(requestedClient, clients):
    """ Return the Client Not Found message string """
    lines = []
    lines.append("Could not find client: " + requestedClient)
    lines.append("Did you mean:")
    lines.append(GetListMessage(FindMatchingClients(requestedClient, clients)))
    return LinesToString(lines)
        
def DisplayOrganizationTypeNotFound(requestedType, organizationTypes):
    """ Display the possible Organization Types """
    print GetOrganizationTypeNotFound(requestedType, organizationTypes)
    
def GetOrganizationTypeNotFoundMessage(requestedType, organizationTypes):
    """ Return the Organization Type Not Found """
    lines = []
    lines.append("Could not find Organization Type: " + requestedType)
    lines.append(GetPossibleOrganizationTypesMessage(organizationTypes))
    return LinesToString(lines)
        
def DisplayOrganizationNotFound(requestedOrganization, organizations):
    """ Display the possible Organization Types """
    print GetOrganizationNotFoundMessage(organizations)
    
def GetOrganizationNotFoundMessage(requestedOrganization, organizations):
    """ Display the possible Organization Types """
    lines = []
    lines.append("Could not find Organization: " + requestedOrganization)
    lines.append(GetPossibleOrganizationsMessage(organizations))
    return LinesToString(lines)
    
def DisplayPossibleOrganizationTypes(organizationTypes):
    """ Display the Possible Organizations """
    print GetPossibleOrganizationTypesMessage(organizationTypes)
    
def GetPossibleOrganizationTypesMessage(organizationTypes):
    """ Display the Possible Organizations """
    lines = []
    lines.append("Possible Organization Types are:")
    lines.append(GetListMessage(organizationTypes))
    return LinesToString(lines)
    
def DisplayPossibleOrganizations(organizations):
    """ Display the Possible Organizations """
    print GetPossibleOrganizationsMessage(organizations)
    
def GetPossibleOrganizationsMessage(organizations):
    """ Display the Possible Organizations """
    lines = []
    lines.append("Possible Organizations are:")
    lines.append(GetListMessage(organizations))
    return LinesToString(lines)
        
def DisplayList(items):
    """ Display a List """
    print GetListMessage(items)
        
def GetListMessage(items):
    """ Get List message String """
    lines = []
    for item in items:
        lines.append("\t{0}".format(item))
    return LinesToString(lines)
    
def LinesToString(lines):
    """ Convert lines into a String """
    return "\n".join(lines)
        
def FindMatchingClients(requestedClient, clients):
    """ Return all matching client names """
    matchingClients = []
    for client in clients:
        if requestedClient.lower() in client.lower():
            matchingClients.append(client)
            
    return matchingClients