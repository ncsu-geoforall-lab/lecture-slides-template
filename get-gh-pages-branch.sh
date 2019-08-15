#!/bin/bash

# fail on first error
set -e

remote=$(git config --get remote.origin.url)

build_dir="build"

# attempt to remove only when exists
# (no error message or error code if it does)
[ ! -e file ] || rm -r $build_dir

# clone only the needed branch
git clone -b gh-pages --single-branch $remote $build_dir
