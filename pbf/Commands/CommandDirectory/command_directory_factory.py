from .command_directory import CommandDirectory

import os

def BuildPBFCoreCommandDirectory(directory):
    """ Build the Core command directory from the directory given """
    localCommandsDirectory = os.path.join(directory, 'Commands')
    return CommandDirectory(os.path.relpath(localCommandsDirectory), os.path.relpath(localCommandsDirectory))