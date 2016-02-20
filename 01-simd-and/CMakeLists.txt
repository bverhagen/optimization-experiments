cmake_minimum_required (VERSION 2.8.1)
project (simd-addition)

# Compilation flags
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

# Include paths

# Lib paths

add_executable(simd-addition simd-and.cpp)
target_link_libraries (simd-addition benchmark pthread c rt)
