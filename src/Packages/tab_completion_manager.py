
def PrintTabCompletion(packages, arguments):
    """  """
    results = []
    if len(arguments) == 0:
        results = GetCategoriesForTabCompletion(packages)
        
    results.sort()
    print " ".join(results)
        
def GetCategoriesForTabCompletion(packages):
    """ Return a list of strings for tab completion """
    return packages.keys()