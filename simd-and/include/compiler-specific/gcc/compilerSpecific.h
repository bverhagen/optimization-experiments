#ifndef __COMPILERSPECIFIC_H__
#define __COMPILERSPECIFIC_H__

#include <cstdint>

// Provisions for defining how likely it is a take a branch
#define likely(x)    __builtin_expect (!!(x), 1)
#define unlikely(x)  __builtin_expect (!!(x), 0)

namespace SimdAnd {
	const size_t BIGGEST_ALIGNMENT = __BIGGEST_ALIGNMENT__;
	typedef std::uint8_t v4uint8_t __attribute__ ((vector_size (__BIGGEST_ALIGNMENT__ / sizeof(std::uint8_t))));	
}

#endif
