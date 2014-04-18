import os
import site
import sys

from pbf.Commands.CommandDirectory.command_directory import CommandDirectory
from pbf.Commands.CommandDirectory.command_directory_factory import BuildPBFCoreCommandDirectory, BuildRequestedCommandDirectories

def FindCommandDirectories(parentDirectory):
    """ Return all the Command Directories under the given parent directory """
    requestedPackages = GetRequestedPacakges()
    sitePackagesRoot = site.getsitepackages()[0]
    return [BuildPBFCoreCommandDirectory(parentDirectory)] + BuildRequestedCommandDirectories(requestedPackages)
    
def GetRequestedPacakges():
    """ Get the Requested packages for the current working directory """
    requestedPackages = []
    try:
        with open('.pbf-properties', 'r') as propertyFile:
            requestedPackages = propertyFile.readlines()
    except IOError:
        pass # If it doesn't exist we just don't add any extra pacakges
    return requestedPackages

def ImportPythonDirectory(directory):
    """ Import Python files from the given directory """
    ImportPythonFilesFromDirectory(directory)
    ImportSubDirectories(directory)
        
def ImportPythonFilesFromDirectory(directory):
    """ Import Python files from the root of the given directory """
    package = directory.getPyhtonPackage()
    for modulename in os.listdir(directory.packageFullPath):
        ImportPythonFile(modulename, package)
        
def ImportSubDirectories(directory):
    """ Import Python files from subdirectories of the given directory """
    for subdirectory in GetImmediateSubdirectories(directory.packageFullPath):
        pacakgePath = os.path.join(directory.packagePath, subdirectory)
        fullpath = os.path.join(directory.packageFullPath, subdirectory)
        ImportPythonDirectory(CommandDirectory(pacakgePath, fullpath))

def GetImmediateSubdirectories(directory):
    return [name for name in os.listdir(directory)
            if os.path.isdir(os.path.join(directory, name))]

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