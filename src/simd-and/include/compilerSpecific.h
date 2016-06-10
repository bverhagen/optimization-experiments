#ifndef __COMPILERSPECIFIC_H__
#define __COMPILERSPECIFIC_H__

#if defined(__GNUC__) || defined(__clang__)
// Provisions for defining how likely it is a take a branch
#define likely(x)    __builtin_expect (!!(x), 1)
#define unlikely(x)  __builtin_expect (!!(x), 0)
#endif

namespace SimdAnd {
#if defined(__GCC__)
	const size_t BIGGEST_ALIGNMENT = __BIGGEST_ALIGNMENT__;
	typedef std::uint8_t v4uint8_t __attribute__ ((vector_size (__BIGGEST_ALIGNMENT__ / sizeof(std::uint8_t))));	

#elif defined(__clang__)
	const size_t BIGGEST_ALIGNMENT = 16;            // Hard code to 16 bytes for now
	typedef std::uint8_t v4uint8_t __attribute__((__aligned__(BIGGEST_ALIGNMENT)));	

#endif
}



#endif
