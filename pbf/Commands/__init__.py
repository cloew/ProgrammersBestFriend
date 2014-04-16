import os
import site
import sys

class CommandDirectory:
    def __init__(self, packagePath, packageFullPath):
        """ Initialize the Command Directory """
        self.packagePath = packagePath
        self.packageFullPath = packageFullPath

def FindCommandDirectories(parentDirectory):
    """ Return all the Command Directories under the given parent directory """
    requestedPackages = []
    try:
        with open('.pbf-properties', 'r') as propertyFile:
            requestedPackages = propertyFile.readlines()
    except IOError:
        pass # If it doesn't exist we just don't add any extra pacakges
    
    sitePackagesRoot = site.getsitepackages()[0]
    localCommandsDirectory = os.path.join(parentDirectory, 'Commands')
    commands = [CommandDirectory(os.path.relpath(localCommandsDirectory), os.path.relpath(localCommandsDirectory))]
    
    for directory in requestedPackages:
        potentialCommandDirectory = os.path.join(directory, "Commands")
        pathToDirectory = os.path.join(sitePackagesRoot, potentialCommandDirectory)
        if os.path.isdir(pathToDirectory):
            commands.append(CommandDirectory(potentialCommandDirectory, pathToDirectory))
        else:
            print "Requested Package has no commands:", potentialCommandDirectory
        
    return commands

def GetImmediateSubdirectories(directory):
    return [name for name in os.listdir(directory)
            if os.path.isdir(os.path.join(directory, name))]
            
def GetPackageName(directory):
    """ Return the Python package Name for the given directory """
    directoryString = directory.replace("\\", "/")
    package_paths = directoryString.split("/")
    if '' in package_paths:
        package_paths.remove('')
    return ".".join(package_paths)

def ImportPythonDirectory(directory):
    """ Import Python files from the given directory """
    ImportPythonFilesFromDirectory(directory)
    ImportSubDirectories(directory)
        
def ImportPythonFilesFromDirectory(directory):
    """ Import Python files from the root of the given directory """
    package = GetPackageName(directory.packagePath)
    for modulename in os.listdir(directory.packageFullPath):
        ImportPythonFile(modulename, package)
        
def ImportSubDirectories(directory):
    """ Import Python files from subdirectories of the given directory """
    for subdirectory in GetImmediateSubdirectories(directory.packageFullPath):
        pacakgePath = os.path.join(directory.packagePath, subdirectory)
        fullpath = os.path.join(directory.packageFullPath, subdirectory)
        ImportPythonDirectory(CommandDirectory(pacakgePath, fullpath))

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
    ImportPythonDirectory(commandsDirectory)