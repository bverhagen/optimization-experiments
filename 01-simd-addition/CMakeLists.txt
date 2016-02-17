cmake_minimum_required (VERSION 2.8.1)
project (simd-addition)

# Set compiler flags
set (CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -Wall -Werror -std=c++11")
set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} -Wall -Werror -std=c++11")

# Include paths
include_directories(../3rdparty/benchmark/include)
include_directories(../common)

# Lib paths
link_directories(../3rdparty/benchmark/src)

add_executable(simd-addition simd-addition-normal.cpp)
target_link_libraries (simd-addition benchmark pthread c rt)
