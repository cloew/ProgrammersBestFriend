from .command_directory import CommandDirectory

import os
import site
SITE_PACKAGES_ROOT = site.getsitepackages()[0]

def BuildPBFCoreCommandDirectory(directory):
    """ Build the Core command directory from the directory given """
    localCommandsDirectory = os.path.join(directory, 'Commands')
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
    global SITE_PACKAGES_ROOT
    commandDirectory = None
    
    potentialCommandDirectory = os.path.join(directory, "Commands")
    pathToDirectory = os.path.join(SITE_PACKAGES_ROOT, potentialCommandDirectory)
    
    if os.path.isdir(pathToDirectory):
        commandDirectory = CommandDirectory(potentialCommandDirectory, pathToDirectory)
    else:
        print "Requested Package has no commands:", potentialCommandDirectory
        
    return commandDirectory