from pbf.helpers.file_helper import IsDirectory
from template_manager import CopyTemplate
import os

class TemplateLoader:
    """ Helper class to load a particular template """
    
    def __init__(self, template, templateFolder=None, defaultFilename=None):
        """ Initialize the template loader """
        self.templateFilename = template
        self.templateFolder = templateFolder
        self.defaultFilename = defaultFilename
        
    def copy(self, filepath, keywords={}):
        """ Copy the Template """
        if IsDirectory(filepath) and self.defaultFilename:
            filepath = os.path.join(filepath, self.defaultFilename)
        CopyTemplate(filepath, self.templateFilename, keywords=keywords, templates_directory=self.templateFolder)