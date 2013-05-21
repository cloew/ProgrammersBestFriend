
def PrintTabCompletion(packages, arguments):
    """  """
    results = []
    if len(arguments) == 0:
        results = GetCategoriesForTabCompletion(packages)
    elif len(arguments) == 1:
        results = GetCommandsForTabCompletion(packages, arguments[0])
        
    results.sort()
    print " ".join(results)
        
def GetCategoriesForTabCompletion(packages):
    """ Return a list of strings for tab completion """
    return packages.keys()
    
def GetCommandsForTabCompletion(packages, category):
    """ Return a list of strings for tab completion """
    return packages[category].keys()