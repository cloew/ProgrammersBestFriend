from pbf.helpers.file_helper import IsDirectory
from pbf.helpers.Project.project_helper import GetParentProjectFromDirectory
from pbf.helpers.Salesforce.salesforce_project_helper import GetCurrentSalesforceProject

from xml.etree.ElementTree import parse, SubElement

import os
import templates.template_manager as template_manager
    
def GenerateBuildProperties(destination):
    """ Generate ANT Build Properties """
    if IsDirectory(destination):
        destination = os.path.join(destination, "build.properties")
        
    project = GetCurrentSalesforceProject()
    keywords = {"%Username%":project.username,
                "%Password%":project.password,
                "%SecurityToken%":project.securityToken}
    template_manager.CopyTemplate(destination, "Salesforce/build.properties", keywords)
    
def LoadBuildXMLTemplateTree():
    """ Returns the XML Tree for the Build XML template """
    return parse(template_manager.GetRealTemplatePath("Salesforce/build.xml"))