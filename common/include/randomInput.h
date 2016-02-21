#ifndef __RANDOM_INPUT_H__
#define __RANDOM_INPUT_H__

#include <cstdlib>
#include <random>
#include <limits>

namespace Common {
	template<typename T>
	inline void randomInput(T* const input, std::size_t nbOfElements) {
		std::default_random_engine generator;
		std::uniform_int_distribution<T> distribution(0);

		for(std::size_t i = 0; i < nbOfElements; ++i) {
			input[i] = distribution(generator);
		}
	}
	
	template<typename T>
	inline void randomInput(T* const input1, T* const input2, std::size_t nbOfElements) {
		randomInput(input1, nbOfElements);
		randomInput(input2, nbOfElements);
	}
}

#endif
