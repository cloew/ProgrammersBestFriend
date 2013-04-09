import os
import sys

def get_immediate_subdirectories(dir):
    return [name for name in os.listdir(dir)
            if os.path.isdir(os.path.join(dir, name))]
            
def GetPackageName(directory):
    """ Return the Python package Name for the given directory """
    package_paths = directory.split("Packages")[1].split("/")
    package_paths.remove('')
    package_paths = ["Packages"] + package_paths
    return ".".join(package_paths)

def ImportPythonDirectory(directory):
    """ Import Python files from the given directory """
    ImportPythonFilesFromDirectory(directory)
    ImportSubDirectories(directory)
        
def ImportPythonFilesFromDirectory(directory):
    """ Import Python files from the root of the given directory """
    package = GetPackageName(directory)
    for modulename in os.listdir(directory):
        ImportPythonFile(modulename, package)
        
def ImportSubDirectories(directory):
    """ Import Python files from subdirectories of the given directory """
    for subdirectory in get_immediate_subdirectories(directory):
        fullpath = os.path.join(directory, subdirectory)
        ImportPythonDirectory(fullpath)

def ImportPythonFile(modulename, package):
    """ Import a Python File """
    if modulename.endswith(".py") and modulename != "__init__.py":
        try:
            module = __import__(package, fromlist=[modulename[:-3]])
        except ImportError as error:
            print "Couldn't import", modulename
            print error
    
packagesDirectory = os.path.dirname(__file__)
ImportPythonDirectory(packagesDirectory)