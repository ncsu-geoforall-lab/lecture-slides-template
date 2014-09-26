#!/usr/bin/env python

# builds pages from source

from __future__ import print_function

import os
import sys
import shutil
import argparse
import re


def error_message(*objs):
    print("ERROR: ", *objs, file=sys.stderr)

def main():
    directories = []
    
    parser = argparse.ArgumentParser(
        description='Copies the common files for all presentations to one directory')
    parser.add_argument('--src-dir', dest='common_srcdir', action='store',
                        help='Directory with common files to copy from')
    parser.add_argument('--dst-dir', dest='common_dstdir', action='store',
                        help='Directory to copy common files to')

    for directory in directories:
        shutil.copytree(directory, os.path.join(destination, directory))

    return 0


if __name__ == '__main__':
    sys.exit(main())
