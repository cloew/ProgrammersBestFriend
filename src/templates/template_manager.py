
def CopyTemplate(filepath, templatepath):
    """ Copy the given template to the lcoation given """
    lines = GetTemplateFileLines(templatepath)
    Save(filepath, lines)

def GetTemplateFileLines(filepath):
    """ Return the lines from given template filepath """
    
def Save(filepath, lines):
    """ Writes the given lines to the file specified at the filepath """
    