cmake_minimum_required (VERSION 2.8.1)
project (common)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

add_library(common STATIC src/performanceUtils.cpp)
