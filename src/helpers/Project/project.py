from helpers.Project.editor import Editor

class Project:
    """ Represents a PBF Project """
    
    def __init__(self, projectXML):
        """ Initialize the Project with the project XML """
        self.projectXML = projectXML
        self.editor = Editor(self.projectXML.find('editor'))
        
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