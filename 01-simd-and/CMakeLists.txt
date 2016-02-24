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
include_directories(include/compiler-specific/gcc)

# Lib paths

add_executable(simd-and-performance src/performance.cpp)
target_link_libraries (simd-and-performance common ${OPTIM_LINKER_BENCHMARK} ${OPTIM_LINKER_STD})

add_executable(simd-and-unittest src/unittest.cpp)
target_link_libraries (simd-and-unittest common ${OPTIM_LINKER_UNITTEST} ${OPTIM_LINKER_STD})
