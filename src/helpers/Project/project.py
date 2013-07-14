
class Project:
    """ Represents a PBF Project """
    
    def __init__(self, projectXML):
        """ Initialize the Project with the project XML """
        self.projectXML = projectXML
        
    @property
    def name(self):
        """ Return the Project name """
        return self.projectXML.find('name').text
        
    @property
    def path(self):
        """ Return the Project path """
        return self.projectXML.find('path').text
        
    @property
    def editor(self):
        """ Return the Project editor """
        return self.projectXML.find('editor').text
        
    def __repr__(self):
        """ Return the string representation """
        return self.name