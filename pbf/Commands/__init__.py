import os

from .extension_loader import ExtensionLoader
from pbf.helpers.PBF.properties_helper import GetRequestedPacakges
    
extLoader = ExtensionLoader(GetRequestedPacakges())
for module in extLoader.load():
    module.importModule("command_map")