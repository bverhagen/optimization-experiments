#!/bin/bash

SUBMODULE_NAME=$(echo "$1" | sed 's/<.*>//g')
echo "Getting submodule commit of ${SUBMODULE_NAME}"

mkdir -p build/3rdparty/submodules
git submodule status | grep ${SUBMODULE_NAME} | sed "s/-//g" | sed "s/^ //g" | cut -f 1 -d " " > build/3rdparty/submodules/${SUBMODULE_NAME}.commit ;
