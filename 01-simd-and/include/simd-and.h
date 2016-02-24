#ifndef __SIMD_AND_H__
#define __SIMD_AND_H__

#include <cstdlib>
#include <cassert>

#include "compilerSpecific.h"
#include "performanceUtils.h"

namespace SimdAnd {
	template<typename T>
	void simdAnd(const T* const input1, const T* const input2, T* const output, std::size_t nbOfElements) noexcept {
		for(std::size_t i = 0; i < nbOfElements; ++i) {
			output[i] = input1[i] & input2[i];
		}
	}

	template<typename T>
	void simdAndForceNormal(const T* const input1, const T* const input2, T* const output, std::size_t nbOfElements) noexcept {
		for(std::size_t i = 0; i < nbOfElements; ++i) {
			output[i] = input1[i] & input2[i];
			if(performanceUtils::alwaysReturnFalse()) {
				performanceUtils::forceUseOfVariable(output[i]);
			}
		}
	}
}

#endif
