cmake_minimum_required (VERSION 2.8.1)
project (benchmark_example_program)

add_executable(benchmark_example_program benchmark.cpp)
target_link_libraries (benchmark_example_program benchmark pthread)
