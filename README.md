Optimization Experiments
------------------------

A play ground for my optimization efforts.

Travis: [![Build Status](https://travis-ci.org/bverhagen/optimization-experiments.svg?branch=master)](https://travis-ci.org/bverhagen/optimization-experiments)
Gitlab: [![build status](https://gitlab.com/bverhagen/optimization-experiments/badges/master/build.svg)](https://gitlab.com/bverhagen/optimization-experiments/commits/master)

Dependencies
------------
- Cmake
- Scons
- Python (both version 2.7.x and 3.x are supported)
- gcc or clang

Note: for certain analysis tools, additional dependencies are required:
- valgrind 
- cppcheck

Usage
-----
- The easiest way is to use the 'exec' script for most general actions. Use
``` $ ./exec -h ```
to see all options
- Typically you want to initialize the repository before starting to work. Use
``` $ ./exec init ``` for this.
