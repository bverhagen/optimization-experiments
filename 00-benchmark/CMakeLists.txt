cmake_minimum_required (VERSION 2.8.1)
project (benchmark_test)

# Set compiler flags
set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -Wall")
set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} -Wall")

# Include paths
include_directories(../3rdparty/benchmark/include)

# Lib paths
link_directories(../3rdparty/benchmark/src)

add_executable(benchmark_test benchmark.cpp)
target_link_libraries (benchmark_test benchmark pthread)
