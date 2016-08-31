#ifndef __COMPILERSPECIFIC_H__
#define __COMPILERSPECIFIC_H__

#if defined(__GNUC__) || defined(__clang__)
// Provisions for defining how likely it is a take a branch
#define likely(x)    __builtin_expect (!!(x), 1)
#define unlikely(x)  __builtin_expect (!!(x), 0)
#endif

namespace SimdAnd {
#if defined(__clang__) && defined(__GNUC__)
	const size_t BIGGEST_ALIGNMENT = 16;            // Hard code to 16 bytes for now

#elif defined(__GNUC__)
	const size_t BIGGEST_ALIGNMENT = __BIGGEST_ALIGNMENT__;

#else
#error Compiler is not supported for vector alignment

#endif

#if defined(__AVX__) || defined(__AVX2__)
#include <avxintrin.h>
typedef __m256i v4uint8_t;

#elif defined(__SSE2__) || defined(__SSE3__) || defined(__SSSE3__) || defined(__SSE4__)
#include <emmintrin.h>
typedef __m128i v4uint8_t;

#elif defined(__MMX__) || defined(__SSE__) 
#include <mmintrin.h>
typedef __m64 v4uint8_t;

#else
typedef std::uint8_t v4uint8_t __attribute__ ((vector_size (sizeof(void*) / sizeof(std::uint8_t))));

#endif

}



#endif
