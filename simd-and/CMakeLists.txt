cmake_minimum_required (VERSION 2.8.1)
project (simd-and)

# Compilation flags
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

if(ENABLE_MMX)
	set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -mmmx")
endif()
if(ENABLE_SSE)
	set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -msse")
endif()
if(ENABLE_SSE)
	set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -msse2")
endif()
if(ENABLE_SSE)
	set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -msse3")
endif()

# Include paths
include_directories(include)

# TODO determine compiler
if ("${CMAKE_CXX_COMPILER_ID}" STREQUAL "Clang")
    include_directories(include/compiler-specific/clang)
elseif ("${CMAKE_CXX_COMPILER_ID}" STREQUAL "GNU")
    include_directories(include/compiler-specific/gcc)
endif()

# Lib paths

# Files
set(PERFORMANCE_FILES   src/benchmark-simd-and-normal.cpp
                        src/benchmark-simd-and-force-normal.cpp
                        src/benchmark-simd-and-vector.cpp)

add_executable(simd-and-performance ${PERFORMANCE_FILES})
target_link_libraries (simd-and-performance common ${OPTIM_LINKER_BENCHMARK} ${OPTIM_LINKER_STD})
install(TARGETS simd-and-performance DESTINATION ${OPTIM_INSTALL_PATH_PERFORMANCE})

add_executable(simd-and-unittest src/unittest.cpp)
target_link_libraries (simd-and-unittest common ${OPTIM_LINKER_UNITTEST} ${OPTIM_LINKER_STD})
install(TARGETS simd-and-unittest DESTINATION ${OPTIM_INSTALL_PATH_UNITTESTS})
