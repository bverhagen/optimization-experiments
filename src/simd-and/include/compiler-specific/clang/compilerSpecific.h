#ifndef __COMPILERSPECIFIC_H__
#define __COMPILERSPECIFIC_H__

#include <cstdint>

// Provisions for defining how likely it is a take a branch
#define likely(x)    __builtin_expect (!!(x), 1)
#define unlikely(x)  __builtin_expect (!!(x), 0)

namespace SimdAnd {
	const size_t BIGGEST_ALIGNMENT = 16;            // Hard code to 16 bytes for now
	typedef std::uint8_t v4uint8_t __attribute__((__aligned__(BIGGEST_ALIGNMENT)));	
}

#endif
