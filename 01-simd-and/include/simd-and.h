#ifndef __SIMD_AND_H__
#define __SIMD_AND_H__

#include <cstdlib>
#include <cassert>

#include "compilerSpecific.h"

namespace SimdAnd {
	template<typename T>
	void simdAndNormal(const T* const input1, const T* const input2, T* const output, std::size_t nbOfElements) noexcept
	{
		for(std::size_t i = 0; i < nbOfElements; ++i) {
			output[i] = input1[i] & input2[i];
		}
	}

	template<typename ActualType, typename SimdType>
	void simdAndForceRegisterSimd(const ActualType* const input1, const ActualType* const input2, ActualType* const output, size_t actualSize) noexcept {
		assert(actualSize * sizeof(ActualType) % sizeof(SimdType) == 0);
		const size_t nbOfSimdIterations = actualSize * sizeof(ActualType)/sizeof(SimdType);

		const SimdType* const simd_input1 = reinterpret_cast<const SimdType* const>(input1);
		const SimdType* const simd_input2 = reinterpret_cast<const SimdType* const>(input2);
		SimdType* const simd_output = reinterpret_cast<SimdType* const>(output);

		for(auto i = 0; i < nbOfSimdIterations; ++i) {
			simd_output[i] = simd_input1[i] & simd_input2[i];
		}
	}

}

#endif
