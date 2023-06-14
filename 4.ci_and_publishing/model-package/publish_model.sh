#!/bin/bash

# Building packages and uploading them to a Gemfury repository
echo "Building packages and uploading them to a Gemfury repository"
GEMFURY_URL=$GEMFURY_PUSH_URL

set -e

DIRS="$@"
BASE_DIR=$(pwd)
SETUP="setup.py"

echo "-----------"
echo "DIRS: $DIRS"
echo "BASE_DIR: $BASE_DIR"
echo "SETUP: $SETUP"
echo "GEMFURY_URL: $GEMFURY_URL"
echo "-----------"

warn() {
    echo "warn"
    echo "$@" 1>&2
}

die() {
    echo "die"
    warn "$@"
    exit 1
}

echo "Building packages and uploading them to GEMFURY_URL"
build() {
    DIR="${1/%\//}"
    echo "------------"
    echo "Checking directory $DIR"
    echo "------------"
    cd "$BASE_DIR/$DIR"
    [ ! -e $SETUP ] && warn "No $SETUP file, skipping" && return
    PACKAGE_NAME=$(python $SETUP --fullname)
    echo "------------"
    echo "Package $PACKAGE_NAME"
    echo "------------"
    python "$SETUP" sdist bdist_wheel || die "Building package $PACKAGE_NAME failed"
    for X in $(ls dist)
    do
        curl -F package=@"dist/$X" "$GEMFURY_URL" || die "Uploading package $PACKAGE_NAME failed on file dist/$X"
    done
}

if [ -n "$DIRS" ]; then
    for dir in $DIRS; do
        build $dir
    done
else
    ls -d */ | while read dir; do
        build $dir
    done
fi