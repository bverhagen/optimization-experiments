cmake_minimum_required (VERSION 2.8.1)
project (simd-and)

# Compilation flags
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

# Include paths
include_directories(include)

# Lib paths

add_executable(simd-and-performance src/performance.cpp)
target_link_libraries (simd-and-performance benchmark pthread c rt)

add_executable(simd-and-unittest src/unittest.cpp)
target_link_libraries (simd-and-unittest catch c rt)
