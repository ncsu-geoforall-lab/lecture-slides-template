#!/usr/bin/env python

# builds pages from source

from __future__ import print_function

import os
import sys
import shutil
import argparse
import re



def ensure_dir(directory):
    """Create all directories in the given path if needed."""
    if not os.path.exists(directory):
        os.makedirs(directory)


def silent_rmtree(filename):
    """Remove the file but do nothing if file does not exist."""
    try:
        shutil.rmtree(filename)
    except OSError as e:
        # errno.ENOENT is "No such file or directory"
        # re-raise if a different error occured
        if e.errno != errno.ENOENT:
            raise

generated_file_info = "<!-- This is a generated file. Do not edit. -->\n"

def error_message(*objs):
    print("ERROR: ", *objs, file=sys.stderr)

def main():
    parser = argparse.ArgumentParser(
        description='Creates one page from several files with individual slides and add header and footer.')
    parser.add_argument('files', metavar='report_directory',
                        type=str, nargs='+',
                        help='Files to be concatenated')
    parser.add_argument('--outdir', dest='outdir', action='store',
                        help='Output directory')
    parser.add_argument('--outfile', dest='outfile', action='store',
                        help='Output directory')
    parser.add_argument('--title', dest='title', action='store',
                        help='Title of the presentation')
    parser.add_argument('--meta-description', dest='meta_description', action='store',
                        help='Description of the material (TODO)')
    parser.add_argument('--meta-author', dest='meta_author', action='store',
                        help='Author of the material (TODO)')
    parser.add_argument('--skip-copy-std-dirs', dest='skip_copy', action='store',
                        help='Do not copy img, audio, video, animations, maps and data directories (TODO)')

    args = parser.parse_args()
    outdir = args.outdir
    outfile = args.outfile
    files = args.files
    title = args.title

    # not used
    css_to_replace = r"['\"]css/"
    js_to_replace = r"['\"]js/"
    lib_to_replace = r"['\"]lib/"

    ensure_dir(outdir)
    outfile = os.path.join(outdir, 'index.html')

    head = 'head.html'
    foot = 'foot.html'
    if not os.path.exists(head):
        return 1
    if not os.path.exists(foot):
        return 1

    with open(outfile, 'w') as outfile:
        with open(head) as infile:
                for line in infile:
                    if title:
                        line = re.sub(r"<title>.*</title>", "<title>" + title + "</title>", line)
                    outfile.write(line)
                    # just to be sure place the comment after doctype and html element
                    # perhaps not needed since we anyway expect HTML5 aware browsers
                    if re.match(r"\s*<html.*>\s*", line):
                        outfile.write(generated_file_info)
        for fname in files:
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)
            outfile.write(generated_file_info)
        with open(foot) as infile:
                for line in infile:
                    outfile.write(line)

    return 0


if __name__ == '__main__':
    sys.exit(main())
