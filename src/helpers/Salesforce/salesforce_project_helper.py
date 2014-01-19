from helpers.file_helper import IsDirectory
from helpers.Project.project_helper import GetParentProjectFromDirectory
from helpers.Salesforce.salesforce_project import SalesforceProject

import os
import templates.template_manager as template_manager

def GetCurrentSalesforceProject():
    """ Get Salesforce Project for the current directory """
    project = GetParentProjectFromDirectory()
    return SalesforceProject(project)
    
def GenerateBuildProperties(destination):
    """ Generate ANT Build Properties """
    if IsDirectory(destination):
        destination = os.path.join(destination, "build.properties")
        
    project = GetCurrentSalesforceProject()
    keywords = {"%Username%":project.username,
                "%Password%":project.password,
                "%SecurityToken%":project.securityToken}
    template_manager.CopyTemplate(destination, "Salesforce/build.properties", keywords)