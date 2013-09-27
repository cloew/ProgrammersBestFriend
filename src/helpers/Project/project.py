from helpers.Project.editor import Editor
from helpers.configuration_helper import GetRelativePathFromConfigurationsDirectory

from xml.etree.ElementTree import SubElement

class Project:
    """ Represents a PBF Project """
    
    def __init__(self, projectXML):
        """ Initialize the Project with the project XML """
        self.projectXML = projectXML
        self.editor = Editor(self.projectXML.find('editor'))
        
    def open(self, filename):
        """ Open the given filename within the context of the current project """
        self.editor.open(filename)
        self.addRecentFile(filename)
        
    def addRecentFile(self, filename):
        """ Add a file to the recently opened section of the Project XML """
        recentFilesElement = self.projectXML.find('recent_files')
        if recentFilesElement is None:
            recentFilesElement = SubElement(self.projectXML, "recent_files")
        recentFileElement = SubElement(recentFilesElement, "recent_file")
        recentFileElement.text = GetRelativePathFromConfigurationsDirectory(filename)
        
    @property
    def name(self):
        """ Return the Project name """
        return self.projectXML.find('name').text
        
    @property
    def path(self):
        """ Return the Project path """
        return self.projectXML.find('path').text
        
    def __repr__(self):
        """ Return the string representation """
        return self.name