cmake_minimum_required (VERSION 2.8.12)
project (optimization-experiments)

option(ENABLE_MMX "Enable MMX instructions" OFF)
option(ENABLE_SSE "Enable SSE instructions" OFF)
option(ENABLE_SSE2 "Enable SSE2 instructions" OFF)
option(ENABLE_SSE3 "Enable SSE3 instructions" OFF)

# Set compiler flags
set(DEFAULT_CXX_COMPILER_OPTIONS "-Wall -Werror")

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${DEFAULT_CXX_FLAGS} -save-temps -fverbose-asm")    # Since this project is about micro benchmarks, enable assembler output by default
set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG}")
set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE}")

# Set linker flags
set(OPTIM_LINKER_BENCHMARK benchmark pthread)
set(OPTIM_LINKER_UNITTEST catch)
set(OPTIM_LINKER_STD c rt)

# Include paths
include_directories (3rdparty/benchmark/include)
include_directories (3rdparty/Catch/single_include)
include_directories(common/include)

# Install path
set(CMAKE_INSTALL_PREFIX ${CMAKE_BINARY_DIR}/bin)
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

set(OPTIM_INSTALL_PATH_UNITTESTS test/unittest)
set(OPTIM_INSTALL_PATH_PERFORMANCE performance)

# TODO: determine target architecture through command line option
include_directories(common/include/i386)

add_subdirectory(3rdparty)
add_subdirectory(catch)
add_subdirectory(common)
add_subdirectory(00-benchmark)
add_subdirectory(simd-and)
