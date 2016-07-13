#!/bin/bash
pmd_version='5.4.2'
pmd_dir="pmd-bin-${pmd_version}"

original_dir=$(pwd)

script_dir="$( dirname "$0" )"
cd ${script_dir}

if [ ! -d ${pmd_dir} ]; then
    if [ ! -f "${pmd_dir}.zip" ]; then
        wget "http://ufpr.dl.sourceforge.net/project/pmd/pmd/${pmd_version}/${pmd_dir}.zip"
    fi

    echo "Unzipping ${pmd_dir}.zip"
    unzip -q "${pmd_dir}.zip"
    ln -fs ${pmd_dir}/bin/run.sh pmd
fi

cd ${original_dir}

if [ ! -z $1 ]; then
    ${original_dir}/${script_dir}/${pmd_dir}/bin/run.sh $@
fi

# How to run: $ ${pmd_dir}/bin/run.sh cpd --files ../../../../src/simd-and/src/*.cpp --minimum-tokens 50 --language cpp
