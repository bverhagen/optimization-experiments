#ifndef __COMPILERSPECIFIC_H__
#define __COMPILERSPECIFIC_H__

#include <cstdint>

namespace SimdAnd {
	const size_t BIGGEST_ALIGNMENT = 16;            // Hard code to 16 bytes for now
	typedef std::uint8_t v4uint8_t __attribute__((__aligned__));	
}

#endif
