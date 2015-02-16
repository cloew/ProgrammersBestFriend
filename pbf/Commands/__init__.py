import os

from pbf.Commands.CommandDirectory.command_directory_factory import BuildPBFCoreCommandDirectory, BuildRequestedCommandDirectories

from pbf.helpers.PBF.properties_helper import GetRequestedPacakges

def FindCommandDirectories(parentDirectory):
    """ Return all the Command Directories under the given parent directory """
    requestedPackages = GetRequestedPacakges()
    return [BuildPBFCoreCommandDirectory(parentDirectory)] + BuildRequestedCommandDirectories(requestedPackages)
    
def ImportPackageCommandMap(directory):
    """ Import the command map for the given PBF Package Directory """
    ImportPythonFile("command_map.py", directory.getPythonPackage())

def ImportPythonFile(modulename, package):
    """ Import a Python File """
    if modulename.endswith(".py") and modulename != "__init__.py":
        try:
            module = __import__(package, fromlist=[modulename[:-3]])
        except ImportError as error:
            print "Couldn't import", modulename
            print error
    
commandsDirectories = FindCommandDirectories(os.path.join(os.path.dirname(__file__), "../"))
for commandsDirectory in commandsDirectories:
    ImportPackageCommandMap(commandsDirectory)