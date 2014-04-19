from .command_directory import CommandDirectory

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
    
    potentialCommandDirectory = os.path.join(directory, "Commands")
    potentialCommandPackagePath = os.path.basename(potentialCommandDirectory)
    if potentialCommandPackagePath == '':
        potentialCommandPackagePath = os.path.basename(potentialCommandDirectory[:-1])
    
    if os.path.isdir(potentialCommandDirectory):
        sys.path.insert(0, directory)
        commandDirectory = CommandDirectory(potentialCommandPackagePath, potentialCommandDirectory)
    else:
        print "Requested Package has no commands:", potentialCommandDirectory
        
    return commandDirectory