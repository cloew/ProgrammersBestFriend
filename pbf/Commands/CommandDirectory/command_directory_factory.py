from .command_directory import CommandDirectory

from pbf.helpers.file_helper import GetBasename, GetDirname
from pbf.helpers.PBF.properties_helper import FindPBFPropertiesDirectory

import os
import site
import sys

SITE_PACKAGES_ROOT = site.getsitepackages()[0]

def BuildPBFCoreCommandDirectory(directory):
    """ Build the Core command directory from the directory given """
    global SITE_PACKAGES_ROOT
    
    if directory.startswith(SITE_PACKAGES_ROOT):
        return CommandDirectory('pbf')
    else:
        return CommandDirectory(os.path.relpath(directory))

def BuildRequestedCommandDirectories(requestedPackages):
    """ Build command directories for each valid requested package """
    commandDirectories = []

    for package in requestedPackages:
        commandDirectory = BuildRequestedCommandDirectory(package)
        if commandDirectory is not None:
            commandDirectories.append(commandDirectory)
    return commandDirectories
    
def BuildRequestedCommandDirectory(directory):
    """ Build the Core command directory from the directory given """
    if directory.startswith('.'):
        return BuildLocalPackageCommandDirectory(directory)
    else:
        return BuildInstalledPackageCommandDirectory(directory)
    
def BuildInstalledPackageCommandDirectory(directory):
    """ Build Command Directory for an installed package """
    global SITE_PACKAGES_ROOT
    commandDirectory = None
    
    potentialCommandMap = os.path.join(directory, "command_map.py")
    pathToCommandMap = os.path.join(SITE_PACKAGES_ROOT, potentialCommandMap)
    
    if os.path.isfile(pathToCommandMap):
        commandDirectory = CommandDirectory(directory)
    else:
        print "Requested Package has no commands:", directory
        
    return commandDirectory
    
def BuildLocalPackageCommandDirectory(directory):
    """ Build Command Directory for an installed package """
    commandDirectory = None
    
    packageRoot = GetBasename(directory)
    
    propertiesDirectory = FindPBFPropertiesDirectory()
    properDirectoryPath = os.path.join(propertiesDirectory, directory)
    potentialCommandMap = os.path.join(properDirectoryPath, "command_map.py")
    
    if os.path.isfile(potentialCommandMap):
        sys.path.insert(0, GetDirname(properDirectoryPath))
        commandDirectory = CommandDirectory(packageRoot)
    else:
        print "Requested Package has no command map:", directory
        
    return commandDirectory