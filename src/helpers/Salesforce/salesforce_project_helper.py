from helpers.Project.project_helper import GetParentProjectFromDirectory

def GetCurrentSalesforceProject()
    """ Get Salesforce Project for the current directory """
    project = GetParentProjectFromDirectory()
    return SalesforceProject