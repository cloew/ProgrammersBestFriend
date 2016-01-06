# from .command_directory import CommandDirectory

from kao_modules import KaoModule
from pbf.helpers.file_helper import GetBasename, GetDirname
from pbf.helpers.PBF.properties_helper import FindPBFPropertiesDirectory

import os
import site
import sys

SITE_PACKAGES_ROOT = site.getsitepackages()[0]

class ExtensionLoader:
    
    def __init__(self, requestedPackages):
        """ Initialize the extension laoder with the requested packages """
        global SITE_PACKAGES_ROOT
        self.requestedPackages = requestedPackages
        self.SITE_PACKAGES_ROOT = SITE_PACKAGES_ROOT
        
    def load(self):
        """ Load the modules required """
        modules = [self.loadCorePBF()]
        return modules + self.loadRequestedPackages()
        
    @property
    def pbf_root(self):
        """ Return the directory containing this implementation of PBF """
        return os.path.join(os.path.dirname(__file__), "../")
        
    def loadCorePBF(self):
        """ Load the Core PBF module so it uses the installed or local version depending on which is being run """
        pbf_root = self.pbf_root
        if pbf_root.startswith(self.SITE_PACKAGES_ROOT):
            return KaoModule('pbf')
        else:
            return self.loadLocalPackage(os.path.normpath(pbf_root))
            
    def loadRequestedPackages(self):
        """ Load the modules for each valid requested package """
        modules = []
        for package in self.requestedPackages:
            module = self.loadRequestedModule(package)
            if module is not None:
                modules.append(module)
        return modules
    
    def loadRequestedModule(self, package):
        """ Load the Requested module based on the package given """
        if package.startswith('.'):
            return self.loadLocalExtension(package)
        else:
            return self.loadInstalledExtension(package)
        
    def loadInstalledExtension(self, package):
        """ Load the module for an installed package """
        module = None
        
        if self.hasCommandMap(os.path.join(self.SITE_PACKAGES_ROOT, package)):
            module = KaoModule(package)
        else:
            print("Requested Package has no commands:", package)
            
        return module
        
    def loadLocalExtension(self, directory):
        """ Load an Extension from a local directory """
        propertiesDirectory = FindPBFPropertiesDirectory()
        properDirectoryPath = os.path.join(propertiesDirectory, directory)
        return self.loadLocalPackage(properDirectoryPath)
        
    def loadLocalPackage(self, directory):
        """ Build Command Directory for an installed package """
        module = None
        packageRoot = GetBasename(directory)
        
        if self.hasCommandMap(directory):
            sys.path.insert(0, GetDirname(directory))
            module = KaoModule(packageRoot)
        else:
            print("Requested Package has no command map:", directory)
            
        return module
        
    def hasCommandMap(self, directory):
        """ Return if the given directory ahs a command map """
        potentialCommandMap = os.path.join(directory, "command_map.py")
        return os.path.isfile(potentialCommandMap)