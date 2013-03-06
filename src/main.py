import sys

import Packages
import Packages.package_manager as package_manager

def main(args):
    """ Run the main file """
    print args
    print package_manager.__Packages__

if __name__ == "__main__":
    main(sys.argv[1:])