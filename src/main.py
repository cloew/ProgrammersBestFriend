import sys

import Packages
import Packages.package_manager as package_manager

def main(args):
    """ Run the main file """
    package_manager.Run(args)

if __name__ == "__main__":
    main(sys.argv[1:])