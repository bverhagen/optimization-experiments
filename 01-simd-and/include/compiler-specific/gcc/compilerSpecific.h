#ifndef __COMPILERSPECIFIC_H__
#define __COMPILERSPECIFIC_H__

#include <cstdint>

namespace SimdAnd {
	const size_t BIGGEST_ALIGNMENT = __BIGGEST_ALIGNMENT__;
	typedef std::uint8_t v4uint8_t __attribute__ ((vector_size (__BIGGEST_ALIGNMENT__ / sizeof(std::uint8_t))));	

	inline void simdAndVector(const v4uint8_t* const input1, const v4uint8_t* const input2, v4uint8_t* const output, std::size_t nbOfElements) noexcept {
		for(std::size_t i = 0; i < nbOfElements; ++i) {
			output[i] = input1[i] & input2[i];
		}
	}
}

#endif
