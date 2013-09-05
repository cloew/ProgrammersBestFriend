from Packages.Core.package_list import PackageList

RootPackageList = PackageList()

__Packages__ = {}

def RegisterPackage(package, category=None):
    """ Registers a Package with the Package Manager """
    if hasattr(package, "category"):
        category = package.category
        
    packageList = GetPackageListForCategory(category)
    
    packageList.addPackage(package.command, package())
    
def GetPackageListForCategory(category):
    """ Returns the Package List for the given category """
    packageList = RootPackageList
    if category is not None and category != '':
        for category in category.split('/'):
            if category in packageList:
                packageList = packageList[category]
            else:
                newPackageList = PackageList(category)
                packageList.addPackage(category, newPackageList)
                packageList = newPackageList
    return packageList
    
def Run(arguments):
    """ Try to Run the given Package """
    if len(arguments) > 0 and arguments[0] == "-c":
        GetTabCompletion(RootPackageList, arguments[1:])
    else:
        RootPackageList.run(arguments)
        
def GetTabCompletion(rootPackageList, arguments):
    """ Return the tab completion strings """
    results = rootPackageList.getTabCompletion(arguments)
        
    results.sort()
    print " ".join(results)