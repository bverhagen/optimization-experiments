#!/bin/bash

echo "Downloading submodule..."
echo $1
echo $2

SUBMODULE_NAME=$(echo "$1" | sed 's/<.*>//g' | sed 's/\.submodule//g')

git submodule init 3rdparty/${SUBMODULE_NAME}
git submodule update
touch $2
