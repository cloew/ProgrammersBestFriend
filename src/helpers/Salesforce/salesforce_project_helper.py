from helpers.Project.project_helper import GetParentProjectFromDirectory
from helpers.Salesforce.salesforce_project import SalesforceProject

def GetCurrentSalesforceProject():
    """ Get Salesforce Project for the current directory """
    project = GetParentProjectFromDirectory()
    return SalesforceProject(project)