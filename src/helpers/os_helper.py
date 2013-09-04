import sys

def GetActionForOS(platformToActions):
    """ Returns the Action for the current operating system.
    If there is no action for th current OS, returns None. """
    currentPlatform = sys.platform
    for platform in platformToActions:
        if currentPlatform.startswith(platform):
            return platformToActions[platform]
    else:
        return None 