#! /usr/bin/python
import sys

from pbf import Commands
from pbf.Commands import command_manager as command_manager

def main(args):
    """ Run the main file """
    command_manager.Run(args)

if __name__ == "__main__":
    main(sys.argv[1:])