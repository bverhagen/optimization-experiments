cmake_minimum_required (VERSION 2.8.11)

set(BENCHMARK_ENABLE_TESTING OFF)
set(BENCHMARK_ENABLE_LTO OFF)       # We do not use LTO for the moment. May be interesting later on.

add_subdirectory (benchmark) 
