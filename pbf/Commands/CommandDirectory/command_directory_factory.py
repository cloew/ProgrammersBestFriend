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
    
    localCommandsDirectory = os.path.join(directory, 'Commands')
    if localCommandsDirectory.startswith(SITE_PACKAGES_ROOT):
        return CommandDirectory('pbf/Commands', localCommandsDirectory)
    else:
        return CommandDirectory(os.path.relpath(localCommandsDirectory), os.path.relpath(localCommandsDirectory))

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
    
    potentialCommandDirectory = os.path.join(directory, "Commands")
    pathToDirectory = os.path.join(SITE_PACKAGES_ROOT, potentialCommandDirectory)
    
    if os.path.isdir(pathToDirectory):
        commandDirectory = CommandDirectory(potentialCommandDirectory, pathToDirectory)
    else:
        print "Requested Package has no commands:", potentialCommandDirectory
        
    return commandDirectory
    
def BuildLocalPackageCommandDirectory(directory):
    """ Build Command Directory for an installed package """
    commandDirectory = None
    
    packageRoot = GetBasename(directory)
    commandPackagePath = os.path.join(packageRoot, "Commands")
    
    propertiesDirectory = FindPBFPropertiesDirectory()
    properDirectoryPath = os.path.join(propertiesDirectory, directory)
    potentialCommandDirectory = os.path.join(properDirectoryPath, "Commands")
    
    if os.path.isdir(potentialCommandDirectory):
        sys.path.insert(0, GetDirname(properDirectoryPath))
        commandDirectory = CommandDirectory(commandPackagePath, potentialCommandDirectory)
    else:
        print "Requested Package has no commands:", directory
        
    return commandDirectory